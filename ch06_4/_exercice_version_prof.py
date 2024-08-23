#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	# Extraire les clés
	# Extraire les clés paires
	return {k for k in dictionary.keys() if k % 2 == 0}

def join_dictionaries(dictionaries):
	return {
		key: value
			for d in dictionaries
				for key, value in d.items()
	}

def dictionary_from_lists(keys, values):
	# Associer les clés et les valeurs.
	# S'arrêter à la fin de la plus petite des deux listes.
	#result = {}
	#for i in range(min(len(keys), len(values))):
	#	result[keys[i]] = values[i]
	#return result
	#return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
	return dict(zip(keys, values))

def get_greatest_values(dictionary, num_values):
	# Extraire les valeurs
	#vals = list(dictionary.values())
	# Ordonner les valeurs
	#vals = sorted(vals, reverse=True)
	# Choisir les num_values plus grands
	return sorted(dictionary.values(), reverse=True)[0:num_values]

def get_sum_values_from_key(dictionaries, key):
	# Extraire les valeurs associés à une clé
	# Faire la somme des valeurs
	#values = []
	#for d in dictionaries:
	#	if key in d:
	#		values.append(d[key])
	return sum([d[key] for d in dictionaries if key in d])


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()

	print("-" * 40)
	print()
	a = ("John", "Charles", "Mike")
	b = ["Jenny", "Christy", "Monica"]
	c = {"Mélissa", "Véronique", "Julie"}
	for ai, bi, ci in zip(a, b, c):
		print(f"{ai}, {bi}, {ci}")
	#for z in zip(a, b, c):
	#	for elem in z:
	#		print(f"{elem} ", end="")
	#	print()

