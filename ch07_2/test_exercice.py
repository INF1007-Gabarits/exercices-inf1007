#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import inspect

from exercice import *


class TestExercice(unittest.TestCase):
	def test_get_fibonacci_number(self):
		values = [i for i in range(10)]
		expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		output = [get_fibonacci_number(i) for i in range(10)]
		self.assertListEqual(
			output,
			expected
		)

	def test_get_fibonacci_sequence(self):
		values = [
			1,
			2,
			5,
			10
		]
		expected = [
			[0],
			[0, 1],
			[0, 1, 1, 2, 3],
			[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		]
		output = [get_fibonacci_sequence(v) for v in values]
		self.assertListEqual(
			output,
			expected
		)

	def test_get_sorted_dict_by_decimals(self):
		values = [
			{
				2: 2.1,
				3: 3.3,
				1: 1.4,
				4: 4.2
			},
			{
				"foo": 42.6942,
				"bar": 42.9000,
				"qux": 69.4269,
				"yeet": 420.1337
			}
		]
		expected = [
			{2: 2.1, 4: 4.2, 3: 3.3, 1: 1.4},
			{'yeet': 420.1337, 'qux': 69.4269, 'foo': 42.6942, 'bar': 42.9}
		]
		output = [get_sorted_dict_by_decimals(v) for v in values]
		self.assertListEqual(
			output,
			expected
		)

	def test_fibonacci_number(self):
		values = [i for i in range(10)]
		expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		output = [fibo for fibo in fibonacci_numbers(10)]
		self.assertListEqual(
			output,
			expected
		)

	def test_build_recursive_sequence_generator(self):
		def fibo_def(last_elems):
			return last_elems[-1] + last_elems[-2]
		fibo = None
		try:
			fibo = build_recursive_sequence_generator([0, 1], fibo_def, False)
		except:
			self.fail("l'appel échoue")
		self.assertTrue(
			inspect.isgeneratorfunction(fibo),
			"L'objet retourné n'est pas un générateur"
		)
		values = [
			1,
			2,
			5,
			10
		]
		expected = [
			[0],
			[0, 1],
			[0, 1, 1, 2, 3],
			[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		]
		output = [[fib for fib in fibo(v)] for v in values]
		self.assertListEqual(
			output,
			expected
		)



if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
