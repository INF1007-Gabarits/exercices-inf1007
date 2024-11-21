#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import Iterator
from math import sqrt
import argparse
import numbers
import sys


def is_prime(num) -> bool:
	"""
	Retourne si un nombre est premier.

	:param num: Le nombre à tester.

	:returns: :code:`True` si premier, :code:`False` sinon
	"""

	for i in range(2, int(round(sqrt(num))) + 1):
		if num % i == 0:
			return False
	return True

def prime_factors(num) -> Iterator[int]:
	"""
	Génère les facteurs premiers d'un nombre.

	:param num: Le nombre à factoriser.
	"""

	for i in range(2, int(num / 2) + 1):
		if is_prime(i) and num % i == 0:
			yield i

def fibonacci_numbers(length) -> Iterator[int]:
	"""
	Génère les nombres de Fibonacci jusqu'à un nombre d'éléments donné.

	:raises TypeError: Si la longueur n'est pas un entier (int).

	:raises ValueError: Si la longueur est négative.

	:param length: Longueur de la suite à générer (doit être un entier ≥ 0).
	"""

	if not isinstance(length, numbers.Integral):
		raise TypeError("Parameter length must be integral (int)")
	if length < 0:
		raise ValueError("Parameter length must be >= 0")

	init_values = [0, 1]
	for elem in init_values[0:length]:
		yield elem

	last_elems = deque(init_values)
	for i in range(len(init_values), length):
		fibo_number = last_elems[-1] + last_elems[-2]
		last_elems.append(fibo_number)
		last_elems.popleft()
		yield fibo_number

def setup_args():
	parser = argparse.ArgumentParser(
		description="Affiche une liste de nombre de Fibonacci.",
		epilog="Tout droits réservés, mais avec réserve."
	)

	# Argument positionnel
	parser.add_argument(
		"num_fibo_numbers",
		type=int,
		help="Les nombres de Fibonacci à afficher.",
	)
	# Argument switch
	parser.add_argument(
		"--fibo-newline",
		action="store_true",
		default=False,
		help="Afficher chaque nombre sur une ligne séparée"
	)
	# Argument optionnel
	parser.add_argument(
		"--mon-autre-arg",
		type=str,
		help="Une autre affaire."
	)

	return parser.parse_args()


def main():
	args = setup_args()

	print("--- Command-line arg ---")
	# L'objet retourné par parse_args a des attributs dont les noms correspondent au nom de l'argument de ligne de commande.
	print("sys.argv:         ", sys.argv)
	print("num_fibo_numbers: ", args.num_fibo_numbers)
	print("fibo_newline:     ", args.fibo_newline)
	print("mon_autre_arg:    ", args.mon_autre_arg)
	print()

	end_str = "\n" if args.fibo_newline else " "
	print("Fibo numbers:", end=end_str)
	for fibo_num in fibonacci_numbers(args.num_fibo_numbers):
		print(fibo_num, end=end_str)

if __name__ == "__main__":
	main()
