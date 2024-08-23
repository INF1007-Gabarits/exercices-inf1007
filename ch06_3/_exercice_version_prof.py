#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(elem) for elem in numbers]

def join_integers(numbers):
	return int("".join([str(elem) for elem in numbers]))

# FONCTION Eratosthène(limite)
def generate_prime_numbers(limit):
 #   premiers = liste vide
	premiers = []
 #   nombres = liste des entiers de 2 à limite
	nombres = [i for i in range(2, limit+1)]
 #   TANT QUE nombres est non vide FAIRE
	while len(nombres) != 0:
 #       Ajouter à premiers le premier entier de nombres
		premiers.append(nombres[0])
 #       nombres = liste des entiers de nombres non multiples du premier
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]
 #   RÉSULTAT premiers
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [string + str(i) for i in range(1, num_combinations+1) if excluded_multiples is None or i % excluded_multiples != 0 for string in strings]

	return [
		string + str(i)
			for i in range(1, num_combinations+1)
			if excluded_multiples is None or i % excluded_multiples != 0
				for string in strings
	]

	# Approche par boucle classiques
	#result = []
	# Pour chaque entier dans la liste de nombre
	#for i in range(1, num_combinations+1):
	#	# Si l'entier n'est pas un multiple de excluded_multiples
	#	if excluded_multiples is None or i % excluded_multiples != 0:
	#		# Pour chaque string dans strings
	#		for string in strings:
	#			# Concaténer la string et le nombre
	#			# Ajouter ça à la liste de résultat
	#			result.append(string + str(i))
	#		# Compréhension de liste intermédiaire
	#		result += [string + str(i) for string in strings]
	## Retourner le résultat
	##return result

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
