"""
Exemple récapitulatif qui inclut les notions du chapitre 11 et de tous les autres.
"""

from _ch8_version_prof import *
from _ch10_version_prof import *
from _ch9_version_prof import start_bot_and_show_plot
from _my_bot_version_prof import MyBot, VotesPlot


def run_ch11_example():
	opts = parse_args()

	config, conf_file = load_config(opts.config_file)
	quotes = load_quotes(opts.quotes_file)
	vote_values = [s.strip() for s in conf_file["votes"]["values"].split(",")]
	ylimit = float(conf_file["votes"]["ylimit"])
	votes_plot = VotesPlot(vote_values, ylimit)

	# TODO: Construire un objet de type `MyBot` avec "logs" comme dossier de journaux, les citations extraites du JSON et le graphique déjà construit.
	bot = MyBot("logs", quotes, votes_plot)
	bot.connect_and_join(config.password, config.nickname, config.channel)
	start_bot_and_show_plot(bot, bot.votes_plot)


if __name__ == "__main__":
	run_ch11_example()
