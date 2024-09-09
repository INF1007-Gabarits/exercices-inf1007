#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	# Extraire le premier prénom
	first_part = name.split("-")[0]
	# Metre en majuscule la première lettre
	capitalized = first_part[0].upper() + first_part[1:].lower()
	# Faire 'Bonjour, <leNom>'
	return "Bonjour, " + capitalized

def get_random_sentence(animals, adjectives, fruits):
	sentence_template = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."

	# Générer un indice aléatoire dans la portée d'indices de chaque tuple. On veut un indice aléatoire différent pour chaque mot.
	animal_word = animals[random.randrange(0, len(animals))]
	adject_word = adjectives[random.randrange(0, len(adjectives))]
	fruit_word = fruits[random.randrange(0, len(fruits))]
	words = [animal_word, adject_word, fruit_word]

	# Approche avec boucle.
	# words = []
	# for word_set in (animals, adjectives, fruits):
	# 	words += [word_set[random.randrange(0, len(word_set))]]

	# Approche bin cool sur une ligne.
	#words = [word_set[random.randrange(0, len(word_set))] for word_set in (animals, adjectives, fruits)]

	return sentence_template % tuple(words)

def format_date(year, month, day, hours, minutes, seconds):
	# Pour la date, il faut s'assurer d'aligner sur deux caractère en remplissant avec un 0.
	formatted_date = f"{year:04}-{month:02}-{day:02}"
	# Pour l'heure, il faut faire la même chose, mais en forçant aussi 3 décimales pour les secondes.
	formatted_time = f"{hours:02}:{minutes:02}:{seconds:06.3f}"
	return formatted_date + " " + formatted_time

def encrypt(text, shift):
	result = ""
	for letter in text:
		encrypted_letter = letter
		# Crypter seulement les caractères alphabétiques.
		if letter.isalpha():
			index = ord(letter.upper()) - ord("A")
			encrypted_index = (index + shift) % 26
			encrypted_letter = chr(ord("A") + encrypted_index)
		result += encrypted_letter
	return result

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangues", "pèches")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.678))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))

