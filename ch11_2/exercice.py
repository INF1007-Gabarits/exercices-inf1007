"""
Chapitre 11.3
"""

import math
from inspect import *

from game import *


def main():
	# TODO: Créer deux personnages avec des stats différents.
	c1 = None
	c2 = None

	# TODO: Créer quelques moves de types différents pour tester les fonctionnalités et les affecter aux deux personnages pour leur donner un gameplay différent.

	# On roule le jeu avec nos deux personnages.
	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

