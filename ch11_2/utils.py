"""
Chapitre 11

Fonctions utilitaires.
"""


import math
import random


def clamp(val, min_val, max_val):
	return max(min_val, min(val, max_val))

def compute_std_damage_output(level, power, attack, defense, crit_chance, random_range):
	"""
	Calcule le dommage selon la formule présentée.
	
	:param level:        Le niveau de l'attaquant
	:param power:        La puissance de l'arme de l'attaquant
	:param attack:       La valeur d'attaque de l'attaquant
	:param defense:      La valeur de défense du défenseur
	:param crit_chance:  La probabilité de coup critique (entre 0 et 1)
	:param random_range: La portée (min, max) du facteur aléatoire
	
	:returns: Un tuple contenant le dommage arrondi à l'entier le plus proche et un booléen indiquant un coup critique
	"""

	level_factor = (2 * level) / 5 + 2
	weapon_factor = power
	atk_def_factor = attack / defense
	critical = random.random() <= crit_chance
	modifier = (2 if critical else 1) * random.uniform(*random_range)
	damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
	return int(round(damage)), critical
