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
		self.fig, self.axes = plt.subplots()
		self.fig.suptitle(title)
		self.axes.set_xlabel("Possible values")
		self.axes.set_ylabel("Num votes")
		self.y_limit = y_limit
		self.axes.set_ylim([0, self.y_limit])
		self.reset_bars(x_data)

	def reset_bars(self, x_data):
		self.x_data = x_data
		self.axes.clear()
		self.y_data = [0] * len(self.x_data)
		self.y_bars = self.axes.bar(self.x_data, self.y_data)

	def update_plot(self):
		# TODO: Reproduire la mise-à-jour du graphique.
		for bar, y in zip(self.y_bars, self.y_data):
			bar.set_height(y)
		self.axes.set_ylim([0, self.y_limit * math.ceil((max(self.y_data)+1)/self.y_limit)])
		self.fig.canvas.draw()
		self.fig.canvas.flush_events()

class MyBot(TwitchBot):
	def __init__(self, logs_folder, quotes, votes_plot):
		# TODO: Construire la classe parent en lui passant le dossier de journaux.
		super().__init__(logs_folder)
		# TODO: Garder le dictionnaire de citations (paramètre `quotes`) dans une variable d'instance.
		self.quotes = quotes
		# TODO: Garder le graphique dans une variable d'instance.
		self.votes_plot = votes_plot

	# TODO: Ajouter une commande "say_hi" (à l'aide du décorateur TwitchBot.new_command) qui répond avec un message de la forme:
	#       "My name is <nom-du-bot>. You killed my father. Prepare to die.", où <nom-du-bot> est le nom du compte utilisé par le chatbot.
	#       Indice : Dans la méthode connect_and_join de TwitchBot, le nom (nickname) du bot est gardé comme attribut.
	@TwitchBot.new_command
	def say_hi(self, cmd: Chatbot.CommandData):
		self.send_privmsg(f"My name is {self.nickname}. You killed my father. Prepare to die.")

	# TODO: Ajouter une commande "quote" qui répond de trois façons selon ce qui suit le nom de la commande dans le message.
	@TwitchBot.new_command
	def quote(self, cmd: Chatbot.CommandData):
		# Si un nom de catégorie est donné (on trouve les paramètres de la commande dans cmd.params) :
		if cmd.params is not None:
			# Si la catégorie est connue, on envoie au hasard une citation venant de cette catégorie si elle est connue.
			if cmd.params in self.quotes:
				self.send_privmsg(random.choice(self.quotes[cmd.params]))
			# Sinon, on envoie un message disant que la catégorie est inconnue (ex. "Unrecognized category 'la_catégorie'")
			else:
				self.send_privmsg(f"Unrecognized category '{cmd.params}'.")
		# Si aucune catégorie n'est fournie, on choisit au hasard une catégorie puis une citation (comme dans l'exemple du chapitre 8)
		else:
			random_category = random.choice(tuple(self.quotes.keys()))
			random_quote = random.choice(self.quotes[random_category])
			self.send_privmsg(random_quote)

	# TODO: Ajouter une commande "vote" qui reproduit le comportement de la même commande de l'exemple du chapitre 9
	@TwitchBot.new_command
	def vote(self, cmd: Chatbot.CommandData):
		vote = cmd.params
		# TODO: Trouver l'index de la valeur votée dans les noms des barres (votes_plot.x_data).
		try:
			index = self.votes_plot.x_data.index(vote)
		except ValueError:
			index = None
		# TODO: Si le vote est reconnu, incrémenter l'élément correspondant des votes obtenus (votes_plot.y_data).
		#       Sinon, envoyer dans le chat un message énumérant les votes possibles.
		if index != None:
			self.votes_plot.y_data[index] += 1
		else:
			self.send_privmsg(f"Possible votes: {', '.join(self.votes_plot.x_data)}")

	# TODO: Ajouter une commande "start_new_vote" qui réinitialise les barres du graphique avec les valeurs en paramètre de la commande (éléments séparés d'un espace).
	@TwitchBot.new_command
	def start_new_vote(self, cmd: Chatbot.CommandData):
		try:
			vote_values = cmd.params.split()
			self.votes_plot.reset_bars(vote_values)
		except:
			self.send_privmsg("!start_new_vote requires choices")

