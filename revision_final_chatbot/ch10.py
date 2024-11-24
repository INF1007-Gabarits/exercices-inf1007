"""
Exemple des notions du chapitre 10.
"""

import argparse
import sys
from collections import namedtuple

from chatbot import *
from twitch_bot import *
from ch8 import *


def parse_args(custom_argv=None):
	arg_parser = argparse.ArgumentParser(
		description="Run custom chatbot.",
		epilog="Made by me."
	)
	arg_parser.add_argument(
		# TODO: Ajouter l'option --config-file
		# TODO: L'argument doit être obligatoire.
		type=str, metavar="INI_FILE",
		help="The INI file containing login and target chat information."
	)
	arg_parser.add_argument(
		# TODO: Ajouter l'option --quotes-file
		# TODO: L'argument doit être obligatoire.
		type=str, metavar="JSON_FILE",
		help="The JSON file containing the various quotes supported by the !quote command."
	)
	argv = custom_argv if custom_argv is not None else sys.argv[1:]
	return arg_parser.parse_args(argv)

def run_ch10_example():
	opts = parse_args()
	# TODO: Passer les noms de fichiers à la fonction du chapitre 8.


if __name__ == "__main__":
	run_ch10_example()
