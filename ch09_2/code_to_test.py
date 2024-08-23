#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import Iterator
from math import sqrt

import argparse


def is_prime(num):
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

	:param length: Longueur de la suite à générer (doit être un entier >= 0).
	"""

	if not isinstance(length, int):
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

def build_recursive_sequence_generator(initial_values, recursive_def, keep_whole_sequence=False):
	def recursive_generator(length):
		for i, elem in enumerate(initial_values):
			if i >= length:
				break
			yield elem
		last_elems = deque(initial_values)
		for i in range(len(initial_values), length):
			fibo_number = recursive_def(last_elems)
			last_elems.append(fibo_number)
			if not keep_whole_sequence:
				last_elems.popleft()
			yield fibo_number
	return recursive_generator

def setup_args():
	parser = argparse.ArgumentParser(description='Affiche les exemples du chapitre 9.')

	parser.add_argument(
		'--arg1',
		type=int,
		help="C'est un paramètre qui sera affiché"
	)
	parser.add_argument(
		"--mon-autre-arg",
		type=str,
		dest="mon_autre_arg",
		help="Une autre affaire."
	)

	return parser.parse_args()

def main():
	args = setup_args()

	print("--- Command-line arg ---")
	arg = None
	print("Argument 1 : ", args.arg1)
	print("Argument 2 : ", args.mon_autre_arg)

	print("--- Generators ---")
	for fibo_num in fibonacci_numbers(1):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2, 1], lambda seq: seq[-1] + seq[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda seq: seq[-2] + seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda seq: seq[-seq[-1]] + seq[-seq[-2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")


if __name__ == "__main__":
	main()
