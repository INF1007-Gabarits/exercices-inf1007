"""
Programmable chatbot
"""

import logging
import sys
import os
import time
from dataclasses import dataclass
import typing

import irc


class Chatbot:
	"""
	Base class for a chatbot.

	It logs every message received and sent using the `logging` module. If no logging is set-up (with `setup_logging`), then a default logger with the default behaviour is used. Messages are logged with the `logging.INFO` level of severity and all logged events have the form :

	[<datetime>][<severity-level>] <event-msg>, with datetime in the form `YYYY-MM-DD HH:MM:SS`. Received messages are prepended with `"> "` and sent messages are prepended with `"< "`.

	The chatbot is meant to recognise commands as PRIVMSG that start with a given command character (commonly "!" or "/") followed by the name of a command (cannot contain spaces) followed by optional parameters.
	"""

	@dataclass
	class CommandData:
		"""
		A command understood by the chatbot.

		:ivar privmsg: The original irc­­.Privmsg object that formed the command.
		:ivar name: The name of the command, without the prepending command character.
		:ivar params: The text following the command.
		"""

		privmsg: irc.Privmsg
		name: str
		params: str

	@dataclass
	class DispatchInfo:
		callback: typing.Any
		cooldown: float # Seconds
		last_call_time: float = 0.0

	def __init__(self, command_char, global_prefix=None, show_password=False):
		self.__irc_client = irc.Client()
		self.global_prefix = global_prefix
		self.show_password = show_password
		self.command_char = command_char
		self.__command_methods = {}
		self.channel = None
		self.logger = logging.getLogger("Chatbot.default")
		self.logger.setLevel(logging.DEBUG)

	@property
	def irc_client(self):
		return self.__irc_client

	@property
	def command_methods(self):
		return self.__command_methods

	def connect(self, host, port, use_ssl=False):
		self.logger.debug(f"Connecting to {host}:{port}...")
		self.irc_client.connect(host, port, use_ssl)
		if use_ssl:
			self.logger.debug(f"Connected using SSL version '{self.irc_client.sock.version()}'")
		else:
			self.logger.debug(f"Connected without SSL")

	def authenticate(self, password, nickname, user_params=None):
		self.send("PASS", password)
		self.send("NICK", nickname)
		if user_params is not None:
			self.send("USER", user_params)

	def join_channel(self, channel):
		self.channel = channel
		sent_msg, num_sent_bytes = self.irc_client.send_join(channel)
		self.logger.info("< " + sent_msg)

	def leave_channel(self):
		if self.channel is not None:
			sent_msg, num_sent_bytes = self.irc_client.send_part(self.channel)
			self.logger.info("< " + sent_msg)
			self.channel = None
		
	def receive_msgs(self):
		msgs = self.irc_client.receive_and_parse()
		for msg in msgs:
			self.logger.info("> " + msg.orig_str)
		return msgs

	def send(self, command, params):
		sent_msg, num_sent_bytes = self.irc_client.send(self.global_prefix, command, params)
		if command == "PASS" and not self.show_password:
			censored_msg = self.irc_client.format_msg(self.global_prefix, command, "*" * len(params))
			self.logger.info("< " + censored_msg)
		else:
			self.logger.info("< " + sent_msg)

		return sent_msg, num_sent_bytes

	def send_privmsg(self, msg):
		sent_msg, num_sent_bytes = self.irc_client.send_privmsg(self.channel, msg)
		self.logger.info("< " + sent_msg)
		return sent_msg, num_sent_bytes

	def register_command(self, command_name, callback, cooldown=0):
		self.command_methods[command_name] = Chatbot.DispatchInfo(callback, cooldown);

	def dispatch_command(self, msg: irc.Privmsg):
		now = time.time()
		parts = msg.text.split(None, 1)
		command_str = parts[0].lower()
		if self.is_known_command(command_str):
			info = self.command_methods[command_str[1:]]
			if now - info.last_call_time >= info.cooldown:
				params = parts[1] if len(parts) == 2 else None
				cmd = Chatbot.CommandData(msg, command_str, params)
				info.last_call_time = now
				info.callback((cmd))

	def setup_logging(self, logs_folder, logger_name, log_to_console=True):
		if not os.path.exists(logs_folder):
			os.mkdir(logs_folder)
		filename = "{}/{}_{}.log".format(
			logs_folder,
			logger_name,
			time.strftime(f"%Y-%m-%d_%H-%M-%S", time.localtime())
		)
		file_handler = logging.FileHandler(filename)
		file_handler.setLevel(logging.DEBUG)
		
		log_fmt = logging.Formatter(fmt="[%(asctime)s][%(levelname)-8s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
		file_handler.setFormatter(log_fmt)
		
		self.logger = logging.getLogger(logger_name)
		self.logger.setLevel(logging.DEBUG)

		self.logger.addHandler(file_handler)

		if log_to_console:
			con_handler = logging.StreamHandler()
			con_handler.setLevel(logging.INFO)
			con_handler.setFormatter(log_fmt)
			self.logger.addHandler(con_handler)

		self.logger.info(f"Log file created in '{filename}'")

	def is_known_command(self, command_str):
		if len(command_str) >= 2:
			return command_str[0] == self.command_char and command_str[1:] in self.command_methods
		else:
			return False
