"""
Un chatbot qui s'identifie et donnes des citations aléatoires.
"""

import random
import math

import matplotlib.pyplot as plt
from chatbot import *
from twitch_bot import *


class VotesPlot:
	def __init__(self, x_data, y_limit, title="Votes in the chat!"):
		# TODO: Reproduire la construction du graphique (code du chapitre 9), mais dans des variables d'instances de l'objet courant.
		self.reset_bars(x_data)

	def reset_bars(self, x_data):
		self.x_data = x_data
		self.axes.clear()
		self.y_data = [0] * len(self.x_data)
		self.y_bars = self.axes.bar(self.x_data, self.y_data)

	def update_plot(self):
		# TODO: Reproduire la mise-à-jour du graphique.
		self.fig.canvas.draw()
		self.fig.canvas.flush_events()

# TODO: Hériter de la classe TwitchBot
class MyBot:
	def __init__(self, logs_folder, quotes, votes_plot):
		# TODO: Construire la classe parent en lui passant le dossier de journaux.
		# TODO: Garder le dictionnaire de citations (paramètre `quotes`) dans une variable d'instance.
		# TODO: Garder le graphique dans une variable d'instance `votes_plot`.
		pass

	# TODO: Ajouter une commande "say_hi" (à l'aide du décorateur TwitchBot.new_command) qui répond avec un message de la forme:
	#       "My name is <nom-du-bot>. You killed my father. Prepare to die.", où <nom-du-bot> est le nom du compte utilisé par le chatbot.
	#       Indice : Dans la méthode connect_and_join de TwitchBot, le nom (nickname) du bot est gardé comme attribut.

	# TODO: Ajouter une commande "quote" qui répond de trois façons selon ce qui suit le nom de la commande dans le message.
		# Si un nom de catégorie est donné (on trouve les paramètres de la commande dans cmd.params) :
			# Si la catégorie est connue, on envoie au hasard une citation venant de cette catégorie si elle est connue.
			# Sinon, on envoie un message disant que la catégorie est inconnue (ex. "Unrecognized category 'la_catégorie'").
		# Si aucune catégorie n'est fournie, on choisit au hasard une catégorie puis une citation (comme dans l'exemple du chapitre 8)
		
	# TODO: Ajouter une commande "vote" qui reproduit le comportement de la même commande de l'exemple du chapitre 9

	# TODO: Ajouter une commande "start_new_vote" qui réinitialise les barres du graphique avec les valeurs en paramètre de la commande (éléments séparés d'un espace).
