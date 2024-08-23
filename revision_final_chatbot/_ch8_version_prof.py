"""
Exemple des notions du chapitre 8.
"""


import configparser
import json
import random
from collections import namedtuple

from chatbot import *
from twitch_bot import *


# Un named tuple est une façon simple de créer des tuples avec des éléments nommés (plutôt que juste des index)
ConfigInfo = namedtuple("ConfigInfo", ["nickname", "password", "channel"])

def load_config(filename):
	config_file = configparser.ConfigParser()
	config_file.read(filename)
	# TODO: Extraire le nom du channel, le nom du compte et le mot de passe (jeton) dans les variables.
	channel = config_file["chat"]["channel"]
	bot_nickname = config_file["login"]["account_name"]
	bot_password = config_file["login"]["account_oauth_token"]
	return ConfigInfo(bot_nickname, bot_password, channel), config_file

def load_quotes(filename):
	# TODO: Charger le contenu du fichier JSON des citations.
	return json.load(open(filename, "r", encoding="UTF-8"))

def build_quotes_callback(bot, quotes):
	def callback(*args):
		# TODO: Choisir une catégorie au hasard.
		random_category = random.choice(tuple(quotes.keys()))
		# TODO: Choisir une citation au hasard dans la catégorie.
		random_quote = random.choice(quotes[random_category])
		# Ou bien :
		#random_category = random.choice(tuple(self.quotes.values()))
		#random_quote = random.choice(random_category)
		bot.send_privmsg(random_quote)
	return callback

def run_ch8_example(config_filename, quotes_filename):
	config, conf_file = load_config(config_filename)
	quotes = load_quotes(quotes_filename)
	bot = TwitchBot("logs")
	bot.register_command("quote", build_quotes_callback(bot, quotes))
	bot.connect_and_join(config.password, config.nickname, config.channel)
	bot.run()


if __name__ == "__main__":
	run_ch8_example("data/config.ini", "data/quotes.json")
