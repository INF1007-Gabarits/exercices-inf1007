"""
Wrapper for IRC protocol

RFC: https://tools.ietf.org/html/rfc1459
"""


import socket
import ssl
from dataclasses import dataclass


@dataclass
class Message:
	"""
	An IRC message. It is at its core made of a prefix, a command and parameters to that command, all space-separated. Messages in a stream are delimited by CR-LF.

	:ivar orig_str: The original full string of the message.
	:ivar prefix: The prefix, can be None.
	:ivar command: The command name.
	:ivar params: The command parameters, can be None.
	"""

	orig_str: str
	prefix: str = None
	command: str = None
	params: str = None

	@classmethod
	def from_str(cls, msg_str):
		msg = msg_str.strip()
		if len(msg) == 0:
			return cls(msg_str)
		if msg.startswith(":"):
			parts = msg.split(None, 2)
			return cls(msg_str, parts[0][1:], parts[1], parts[2] if len(parts) == 3 else None)
		else:
			parts = msg.split(None, 1)
			return cls(msg_str, None, parts[0], parts[1] if len(parts) == 2 else None)

@dataclass
class Privmsg:
	"""
	The main purpose of the IRC protocol is to provide a base for clients to communicate with each other. Messages with the PRIVMSG command are the main messages which actually perform delivery of a text message from one client to another. This is how users chat with each other.

	A PRIVMSG typically has the form `<prefix> PRIVMSG <#|&><channel> :<text>` (https://tools.ietf.org/html/rfc1459#section-4.4.1)

	:ivar orig_str: The original full string of the message
	:ivar prefix: The prefix, can be None. Clients usually do not need to add a prefix when sending messages.
	:ivar channel: The channel name, without the # or & character.
	:ivar text: The message text, without the beginning colon.
	"""

	orig_str: str
	prefix: str = None
	channel: str = None
	text: str = None

	@classmethod
	def from_str(cls, msg_str):
		return cls.from_irc_msg(Message.from_str(msg_str))

	@classmethod
	def from_irc_msg(cls, irc_msg):
		privmsg = cls(irc_msg.orig_str)
		channel_str, text_str = irc_msg.params.split(None, 1)
		privmsg.prefix = irc_msg.prefix
		privmsg.channel = channel_str[1:]
		privmsg.text = text_str[1:] if text_str[0] == ":" else text_str
		return privmsg


class Client:
	def __init__(self, channel_char="#"):
		self.ssl_context = ssl.create_default_context()
		self.sock = None
		self.channel_char = "#"

	def connect(self, host, port, use_ssl=False):
		self.sock = socket.create_connection((host, port))
		if use_ssl:
			self.sock = self.ssl_context.wrap_socket(self.sock, server_hostname=host)
		self.sock.settimeout(0)

	def disconnect(self):
		if self.sock is not None:
			self.sock.close()
			self.sock = None

	def send_join(self, channel):
		return self.send(None, "JOIN", self.channel_char + channel)

	def send_part(self, channel):
		return self.send(None, "PART", self.channel_char + channel)

	def send_privmsg(self, channel, msg):
		return self.send(None, "PRIVMSG", f"{self.channel_char}{channel} :{msg}")

	def receive_and_parse(self):
		msgs = self.receive()
		return [Message.from_str(msg) for msg in msgs]

	def send(self, msg_prefix, msg_command, command_params, newline_replacement = " "):
		msg_str = self.format_msg(msg_prefix, msg_command, command_params, newline_replacement)
		num_sent_bytes = self.sock.send(bytes("\r\n" + msg_str + "\r\n", "UTF-8"))
		return msg_str, num_sent_bytes

	def format_msg(self, msg_prefix, msg_command, command_params, newline_replacement = " "):
		command_params = newline_replacement.join(command_params.split())
		msg_str = ""
		if msg_prefix is not None:
			msg_str += f":{msg_prefix} "
		msg_str = f"{msg_command} {command_params}"
		return msg_str

	def receive(self):
		msg_list = []
		data = b""
		while True:
			try:
				rec_bytes = self.sock.recv(4096)
			except ssl.SSLWantReadError:
				rec_bytes = b""
			if len(rec_bytes) == 0:
				break
			data += rec_bytes
			lines = data.split(b"\r\n")
			if lines[-1] != b"":
				lines = lines[:-1]
				data = lines[-1]
			else:
				data = b""
			for l in lines:
				if l != b"":
					msg_list.append(l.decode("UTF-8"))
		return msg_list

