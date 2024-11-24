"""
Exemple des notions du chapitre 9.
"""

import argparse
import sys
from collections import namedtuple
import math
import threading
import time

import matplotlib.pyplot as plt

from chatbot import *
from twitch_bot import *
from ch8 import *


VotesPlot = namedtuple("VotesPlot", ["figure", "axes", "x_data", "y_data", "update_plot"])

def build_votes_plot(x_data, y_limit):
	y_data = [0] * len(x_data)
	fig, ax = plt.subplots()
	# TODO: Donner un titre à la figure.
	# TODO: Donner un nom aux deux axes.
	# TODO: Établir la portée de l'axe y de 0 à y_limit.
	# TODO: Créer un axe d'histogramme (bar).
	y_bars = ...
	
	def update_plot():
		# TODO: Mettre à jour les barres de l'histogramme (y_bars) avec les données (y_data).
		# TODO: Mettre à jour la portée de l'axe verticale au multiple de y_limit le plus proche de la valeur maximale en y.

		fig.canvas.draw()
		fig.canvas.flush_events()

	return VotesPlot(fig, ax, x_data, y_data, update_plot)

def build_vote_callback(bot, votes_plot: VotesPlot):
	def callback(cmd: Chatbot.CommandData):
		vote = cmd.params
		# TODO: Trouver l'index de la valeur votée dans les noms des barres (votes_plot.x_data).
		# TODO: Si le vote est reconnu, incrémenter l'élément correspondant des votes obtenus (votes_plot.y_data).
		#       Sinon, envoyer dans le chat un message énumérant les votes possibles.

	return callback

def start_bot_and_show_plot(bot, votes_plot):
	thr = threading.Thread(target=bot.run)
	thr.start()

	plt.show(block=False)
	while thr.is_alive():
		try:
			votes_plot.update_plot()
			time.sleep(1.0/30)
		except BaseException as e:
			bot.logger.error(str(e))
			bot.stop()
		except:
			bot.stop()
	thr.join()

def run_ch9_example():
	config, conf_file = load_config("data/config.ini")

	bot = TwitchBot("logs")
	# TODO: Extraire les valeurs de votes à partir du fichier de configuration.
	vote_values = ...
	# TODO: Extraire la limite de l'axe y à partir du fichier de configuration.
	ylimit = ...
	# TODO: Construire le graphique.
	votes_plot = ...
	# TODO: Construire le callback de vote.
	update_plot_data = ...
	# TODO: Enregistrer la commande !vote.
	bot.register_command(...)

	bot.connect_and_join(config.password, config.nickname, config.channel)
	start_bot_and_show_plot(bot, votes_plot)


if __name__ == "__main__":
	run_ch9_example()
