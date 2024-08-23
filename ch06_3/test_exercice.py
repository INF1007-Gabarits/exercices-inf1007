#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
	def test_get_maximums(self):
		values = [
			[[1,2,3], [6,5,4], [10,11,12], [8,9,7]]
		]
		expected = [
			[3, 6, 12, 9]
		]
		output = [exercice.get_maximums(v) for v in values]
		self.assertEqual(
			expected,
			output,
			"Mauvais compte de maximums."
		)

	def test_join_integers(self):
		values = [
			[111, 222, 333],
			[69, 420]
		]
		expected = [
			111222333,
			69420,
		]
		output = [exercice.join_integers(v) for v in values]

		self.assertIs(
			type(output[0]),
			int,
			"Il faut retourner des int"
		)
		self.assertListEqual(
			output,
			expected,
			"Mauvaise concaténation"
		)

	def test_generate_prime_numbers(self):
		values = [
			2,
			17,
		]
		expected = [
			[2],
			[2, 3, 5, 7, 11, 13, 17]
		]
		output = [exercice.generate_prime_numbers(v) for v in values]

		self.assertListEqual(
			output,
			expected,
			"Mauvaise génération de nombres premiers"
		)

	def test_combine_strings_and_numbers(self):
		values = [
			(["A", "B"], 2, None),
			(["A", "B"], 5, 2)
		]
		expected = [
			['A1', 'B1', 'A2', 'B2'],
			['A1', 'B1', 'A3', 'B3', 'A5', 'B5']
		]
		output = [exercice.combine_strings_and_numbers(*v) for v in values]

		self.assertListEqual(
			output,
			expected,
			"Mauvaise génération de nombres premiers"
		)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
