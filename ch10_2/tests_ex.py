#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import inspect

from code_to_test import *


class PrimeTests(unittest.TestCase):
	def test_prime(self):
		value = 2
		expected = True
		result = is_prime(value)
		self.assertEqual(result, expected)

class FibonacciTests(unittest.TestCase):
	def test_is_generator(self):
		self.assertTrue(
			inspect.isgeneratorfunction(fibonacci_numbers),
			"La fonction n'est pas un générateur"
		)

	def test_valid_lengths(self):
		# Classes d'équivalences de valeurs pour length
		#	Valides:
		#		A: = 0
		#		B: = 1, 2
		#			min: 1
		#			max: 2
		#		C: > 2
		#			min: 3
		#			échantillon: 5
		#			max: infini (donc à ignorer car impossible à tester)
		#	Invalides:
		#		D: < 0
		#			max: -1
		#			échantillon : -5
		#			min: -∞ (pas testé)
		#		E: pas un int
		#			valeur limite: None
		#			échantillon: "henlo"

		values = [
			0,
			1,
			2,
			3,
			5
		]
		expected = [
			[],
			[0],
			[0, 1],
			[0, 1, 1],
			[0, 1, 1, 2, 3]
		]
		output = [[fibo for fibo in fibonacci_numbers(v)] for v in values]
		
		self.assertListEqual(
			output,
			expected
		)

	def test_invalid_lengths(self):
		values = [
			-1,
			-5,
			None,
			"henlo"
		]
		expected_except = [
			ValueError,
			ValueError,
			TypeError,
			TypeError
		]

		for v, e in zip(values, expected_except):
			with self.assertRaises(e):
				fibo_series = [fibo for fibo in fibonacci_numbers(v)]

	#def test_build_recursive_sequence_generator(self):
	#	def fibo_def(last_elems):
	#		return last_elems[-1] + last_elems[-2]
	#	fibo = None
	#	try:
	#		fibo = build_recursive_sequence_generator([0, 1], fibo_def, False)
	#	except:
	#		self.fail("l'appel échoue")
	#	self.assertTrue(
	#		inspect.isgeneratorfunction(fibo),
	#		"L'objet retourné n'est pas un générateur"
	#	)
	#	values = [
	#		1,
	#		2,
	#		5,
	#		10
	#	]
	#	expected = [
	#		[0],
	#		[0, 1],
	#		[0, 1, 1, 2, 3],
	#		[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	#	]
	#	output = [[fib for fib in fibo(v)] for v in values]
	#	self.assertListEqual(
	#		output,
	#		expected
	#	)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=3).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
