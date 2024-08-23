"""
Chatbot for Twitch
"""

import os
import logging
import time
import functools
import inspect
from dataclasses import dataclass

from irc import *
from chatbot import Chatbot


class TwitchBot(Chatbot):
	"""
	Chat bot base class made specifically for Twitch

	In derived classes, commands handlers (responding to '!<command>' messages) are registered using the `@TwitchBot.new_command` decorator and must be methods that take a `Chatbot.CommandData` as parameter (along with self). The method name is used as command name and is not case-sensitive. The method docstring is used as help text if user types !help <command>. The name of the command (preceded or not by !) can be ommitted and will be inserted automatically. The `cooldown` parameter of the decorator is used to limit the frequency at which the command is triggered. It is a cooldown period after each dispatched call.

	Example: 
	.. code-block:: python
		class SomeBot(TwitchBot):
			@TwitchBot.new_command
			def my_cmd(self, cmd: Chatbot.CommandData):
				'''{some_required_param} [some_optional_param]'''
				# Do something
			@TwitchBot.new_command(cooldown=3.0)
			def my_cmd2(self, cmd: Chatbot.CommandData):
				'''{some_required_param} [some_optional_param]'''
				# Do something, but at most every 3 seconds because of cooldown

	In this case, the command is activated by the message !my_cmd or !my_cmd2 followed or not by something.
	!help my_cmd will send the help string (so '!my_cmd {some_required_param} [some_optional_param]').
	Note that the !my_cmd was inserted automatically.

	If a command callback is registered manually with `register_command`, it must only take one argument which is a `Chatbot.CommandData` (already be bound to self in case of a method).
	"""

	@staticmethod
	def new_command(func=None, /, *, cooldown=0):
		def decorator(fn):
			fn.command_cooldown = cooldown
			fn.is_twitchbot_command_function = True
			return fn
		# Trick to check if decorator was applied without arguments. If the first argument is None, then it was called with arguments.
		if func is None:
			return decorator
		else:
			return decorator(func)

	TWITCH_CHAT_URL = "irc.chat.twitch.tv"
	TWITCH_CHAT_PORT = 6697
	TWITCH_TEXT_LEN_MAX = 500
	HELP_COMMAND_NAMES = ("commands", "help")
	DEFAULT_HELP_COOLDOWN = 3.0

	def __init__(self, logs_folder, log_to_console=True, pokemon_exception_handling=False, show_password=False):
		super().__init__(command_char="!", show_password=show_password)
		self.logs_folder = logs_folder
		self.log_to_console = log_to_console
		self.pokemon_exception_handling=pokemon_exception_handling
		self.authenticated = False
		self._setup_commands()

	def connect_and_join(self, password, nickname, channel):
		self.authenticated = False
		self.nickname = nickname
		self.channel = channel

		self.setup_logging(self.logs_folder, f"TwitchBot.{self.channel}.{self.nickname}", True)

		self.connect(TwitchBot.TWITCH_CHAT_URL, TwitchBot.TWITCH_CHAT_PORT, True)

		self.authenticate(password, nickname)
		while (msgs := self.receive_msgs()) == []:
			pass
		for msg in msgs:
			if "login authentication failed" in msg.params.lower():
				self.logger.error("Authentication to server failed")
				return
		self.authenticated = True

		# Membership (Twitch verbosity stuff)
		membership_requests = (
			"membership",
			#"tags",
			"commands"
		)
		for req in membership_requests:
			self.send("CAP", f"REQ :twitch.tv/{req}")
			while self.receive_msgs() == []:
				pass
			self.receive_msgs()

		self.join_channel(channel)
		time.sleep(0.5)
		while self.receive_msgs() == []:
			pass

		self.logger.debug("Done connecting.")

	def run(self):
		if not self.authenticated:
			self._leave_and_disconnect()
			self.logger.error("Tried to run without connecting and authenticating first.")
			return

		self.logger.debug("Listening to chat for commands...")
		while True:
			try:
				time.sleep(0.010) # Just to yield control of the thread
				msgs = self.receive_msgs()
				for msg in msgs:
					if msg.command == "PING":
						self.send("PONG", msg.params)
					elif msg.command == "PRIVMSG":
						privmsg = Privmsg.from_irc_msg(msg)
						if privmsg.channel == self.channel:
							self.dispatch_command(privmsg)
			except ConnectionError as e:
				self.logger.error(str(e))
				break
			except Exception as e:
				self.logger.error(f"{type(e).__name__}: {str(e)}")
				if not self.pokemon_exception_handling:
					break
			except KeyboardInterrupt:
				self.logger.error(f"Caught KeyboardInterrupt, shutting down")
				break
			except:
				self.logger.error("Unknown exception caught")
				break
		self._leave_and_disconnect()

	def send_supported_commands(self, cmd: Chatbot.CommandData):
		if cmd.params is None:
			msg = "I can do all this: "
			msg += ", ".join(["!" + name for name in self.command_methods.keys()])
			self.send_privmsg(msg)
			help_commands_list = " or ".join(["!" + e for e in TwitchBot.HELP_COMMAND_NAMES])
			self.send_privmsg(f"Sending {help_commands_list} followed by a command gives usage detail.")
		else:
			requested_command = cmd.params.split(None, 1)[0].lstrip("!").lower()
			if requested_command in self.command_methods:
				msg = self.command_methods[requested_command].callback.__doc__
				self.send_privmsg(msg)
			else:
				self.send_privmsg(f"I don't know what '{requested_command}' is.")

	def send_privmsg(self, msg):
		sent_msg, num_sent_bytes = super().send_privmsg(msg)
		text_length = len(Privmsg.from_str(sent_msg).text)
		if text_length > TwitchBot.TWITCH_TEXT_LEN_MAX:
			self.logger.warning(f"Message length {text_length} > {TwitchBot.TWITCH_TEXT_LEN_MAX}")
		return sent_msg, num_sent_bytes

	def register_command(self, command_name, callback, cooldown=0):
		command_name = command_name.lower().strip()
		if command_name[0] == self.command_char:
			command_name = command_name[1:]
		copied_callback = functools.partial(callback)
		copied_callback.__doc__ = TwitchBot.format_usage_docstring(command_name, callback.__doc__)
		super().register_command(command_name.lower(), copied_callback, cooldown)

	@staticmethod
	def get_user(cmd: Chatbot.CommandData):
		return cmd.privmsg.prefix.split("!", 1)[0]

	@staticmethod
	def format_usage_docstring(method_name, docstr):
		new_docstr = "Usage: "
		if docstr is None or docstr.strip() == "":
			new_docstr += "!" + method_name
		else:
			if docstr.split(None, 1)[0].lstrip("!") == method_name:
				new_docstr += "!" + docstr
			else:
				new_docstr += "!" + method_name + " " + docstr
		return new_docstr

	def _setup_commands(self):
		self._register_help_commands()

		command_functions = inspect.getmembers(
			self,
			lambda fn: hasattr(fn, "is_twitchbot_command_function") and fn.is_twitchbot_command_function
		)
		for name, method in command_functions:
			self.register_command(name.lower(), method, method.command_cooldown)

	def _register_help_commands(self):
		help_fn = functools.partial(TwitchBot.send_supported_commands, self)
		help_fn.__doc__ = "Shows the usage for a command."
		for name in TwitchBot.HELP_COMMAND_NAMES:
			self.register_command(name, help_fn, TwitchBot.DEFAULT_HELP_COOLDOWN)

	def _leave_and_disconnect(self):
		ch = self.channel
		self.leave_channel()
		self.logger.debug(f"Left channel {ch}")
		self.irc_client.disconnect()
		self.logger.debug(f"Disconnected")

