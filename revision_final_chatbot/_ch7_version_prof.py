"""
Exemple des notions du chapitre 7.
"""

from chatbot import *
from twitch_bot import *


def build_say_hi_callback(bot: TwitchBot, message):
	# TODO: Créer et retourner une fonction qui prend un paramètre (ignoré).
	#       Cette fonction envoie `message` dans le chat à l'aide de la méthode `send_privmsg` du paramètre `bot`.
	def callback(*args):
		bot.send_privmsg(message)
	return callback

def run_ch7_example():
	bot = TwitchBot("logs")
	# TODO: Construire deux callbacks avec le bot et un message de votre choix pour chacun.
	callback1 = build_say_hi_callback(bot, "Manon, pèse su'l piton!")
	callback2 = build_say_hi_callback(bot, "Haha! 'Tis I, the chatbot!")
	# TODO: Enregister les callback : un sous la commande "say_bonjour" et l'autre "say_hi".
	bot.register_command("say_bonjour", callback1)
	bot.register_command("say_hi", callback2)
	# TODO: Mettre votre jeton (incluant le "oauth:") et le nom du compte Twitch associé.
	bot.connect_and_join("oauth:...", "...", "chosson")
	bot.run()


if __name__ == "__main__":
	run_ch7_example()
