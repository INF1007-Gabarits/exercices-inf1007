#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index : list) :
	return (0 if index == 0 
		 else 1 if index == 1 
		 else get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2))

def get_fibonacci_sequence(length : int) :
	sequence = []

	for i in range(length) :
		if i == 0 :
			sequence.append(0)
		elif i == 1 :
			sequence.append(1)
		else :
			sequence.append(sequence[i - 1] + sequence[i - 2])
	
	return sequence

def get_sorted_dict_by_decimals(elems):
	return dict(sorted(elems.items(), key=lambda e: e[1] % 1.0))

def fibonacci_numbers(length):
	avantDernier = 0
	dernier = 1
	suivant = avantDernier + dernier
	yield avantDernier
	yield dernier

	while dernier < length :
		#print(avantDernier, dernier)
		suivant = avantDernier + dernier
		yield suivant

		avantDernier += 1
		dernier += 1

def build_recursive_sequence_generator(TODO):
	pass


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
