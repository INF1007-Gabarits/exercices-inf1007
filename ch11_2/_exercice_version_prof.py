"""
Chapitre 11
"""

import math
from inspect import *

from game import *
from character import *
from _spells_version_prof import *


def main():
	# Deux persos
	c1 = Character("Äpik", 500, 150, 70, 70)
	c2 = Character("Gämmör", 550, 100, 120, 60)
	
	# Un move de chaque type qu'on a créé.
	bfg = SimpleDamagingMove("BFG", 100, 69)
	suck = DrainingMove("Big Sucky", 70, 0.5, 30)
	thiccer = IntensifyingMove("Thiccer and THICCER", 50, 5, 20)
	feels_good = HealingMove("Feels Good Man", 0.05, 4, 20)

	# Affecter les moves aux personnages.
	c1.main_move = bfg
	c1.secondary_move = thiccer
	c2.main_move = suck
	c2.secondary_move = feels_good

	# On roule le jeu avec nos deux personnages.
	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

