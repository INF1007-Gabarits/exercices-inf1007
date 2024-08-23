"""
Chapitre 11

Code simulant un combat.
"""


import os
import sys
import select
import utils

from readchar import readchar, readkey

from character import Character, Move


def run_battle(c1: Character, c2: Character):
	# Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	c2 = c2
	num_turns = 1
	
	for m in c1.moves + c2.moves:
		if m is not None:
			m.on_combat_begin()
	
	while True:
		begin_turn(c1, c2)

		dead_character = apply_turn(c1, c2)
		if dead_character is not None:
			print_characters(c1, c2)
			print(f"{dead_character.name} is sleeping with the fishes.\n")
			break
		
		num_turns += 1
	# Retourner nombre de tours effectués
	return num_turns

def begin_turn(c1, c2):
	print_characters(c1, c2)
	
	# On collecte les messages (si applicable) retournés par les `on_turn_begin`.
	turn_begin_messages = []
	for m in c1.moves + c2.moves:
		if m is not None:
			msg = m.on_turn_begin()
			if msg is not None and not msg.isspace():
				turn_begin_messages.append(msg.strip())

	# Si on a au moins un message non nul, on affiche le dialogue en attendant une touche.
	if len(turn_begin_messages) != 0:
		print("\n".join(turn_begin_messages))
		print("\nEnter a key to continue...")
		readkey()

def apply_turn(c1, c2):
	attacker = c1
	defender = c2
	
	for _ in range(2):
		# Afficher les infos de personnage en haut de l'écran
		print_characters(c1, c2)
		
		# Chosir et appliquer l'action
		select_and_apply_action(attacker, defender)
		print("Enter a key to continue...")
		readkey()
		
		# Si un personnage est mort, on le retourne
		dead_character = defender if defender.hp == 0 else attacker if attacker.hp == 0 else None
		if dead_character is not None:
			return dead_character
		
		# Échanger attaquant/défendeur
		attacker, defender = defender, attacker
	
	return None

def print_characters(c1, c2):
	ALIGNMENT = 20
	
	# Pas la façon la plus propre d'effacer le terminal, mais bon je vais pas importer curses juste pour une ligne de code.
	os.system("cls" if os.name == "nt" else "clear")
	
	print(f"{c1.name:<{ALIGNMENT}} lvl {c1.level:<3} | {c2.name:<{ALIGNMENT}} lvl {c2.level:<3}")
	char_strings = [f"HP: {c.hp:>3}/{c.max_hp:>3}" for c in (c1, c2)]
	print(f"{char_strings[0]:<{ALIGNMENT+8}} | {char_strings[1]:<{ALIGNMENT+8}}")
	print("¯" * ((ALIGNMENT+8)*2+3))

def select_and_apply_action(attacker, defender):
	print(f"Select move for {attacker.name}:")
	for i, m in enumerate(attacker.moves):
		print(f"  {i}: {m.name if m is not None else 'N/A'}")
	print()
	while True:
		try:
			print("> ", end="")
			action_index = readkey()
			if action_index.isalnum():
				print(action_index)
			# Appliquer l'action
			msg = attacker.use_move(int(action_index), defender)
			print("\n" + msg + "\n")
		except (ValueError, IndexError):
			print("No can do, try something else")
		else:
			return
