"""
Chapitre 11.1

Code simulant un combat.
"""


import utils

from character import Character


def run_battle(c1: Character, c2: Character):
	# Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	num_turns = 1
	print(f"{attacker.name} starts a battle with {defender.name}!\n")
	while True:
		# Appliquer l'attaque
		msg = attacker.apply_turn(defender)
		print(msg + "\n")
		# Si un personnage est mort
		dead_character = defender if defender.hp == 0 else attacker if attacker.hp == 0 else None
		if dead_character is not None:
			print(f"{dead_character.name} is sleeping with the fishes.")
			break
		num_turns += 1
		# Échanger attaquant/défendeur
		attacker, defender = defender, attacker
	# Retourner nombre de tours effectués
	return num_turns
