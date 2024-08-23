#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
	def test_get_even_keys(self):
		values = [
			{
				69: "Yeet",
				420: "YeEt",
				9000: "YEET",
			}
		]
		expected = [
			{9000, 420}
		]
		output = [exercice.get_even_keys(v) for v in values]

		self.assertIs(
			type(output[0]),
			set,
			"Il faut retourner un set"
		)
		self.assertListEqual(
			expected,
			output,
			"Mauvaise extraction de clés paires."
		)

	def test_join_dictionaries(self):
		values = [
			{
				69: "Yeet",
				420: "YeEt",
				9000: "YEET",
			},
			{
				0xBEEF: "doot",
				0xDEAD: "DOOT",
				0xBABE: "dOoT"
			}
		]
		expected = {
			69: 'Yeet',
			420: 'YeEt',
			9000: 'YEET',
			48879: 'doot',
			57005: 'DOOT',
			47806: 'dOoT'
		}
		output = exercice.join_dictionaries(values)

		self.assertEqual(
			output,
			expected,
			"Mauvaise concaténation de dictionnaires."
		)

	def test_dictionary_from_lists(self):
		values = (
			[
				"D'OH!",
				"d'oh",
				"DOH!"
			],
			[
				"NICE!",
				"nice",
				"nIcE",
				"NAIIIIICE!"
			]
		)
		expected = {
			"D'OH!": 'NICE!',
			"d'oh": 'nice',
			'DOH!': 'nIcE'
		}
		output = exercice.dictionary_from_lists(*values)

		self.assertEqual(
			output,
			expected,
			"Mauvaise génération de dictionnaires."
		)

	def test_get_greatest_values(self):
		values = {
			"nice": 69,
			"nice bro": 69420,
			"AGH!": 9000,
			"dude": 420,
			"git gud": 1337
		}
		expected = [
			[69420],
			[69420, 9000, 1337]
		]
		output = [exercice.get_greatest_values(values, n) for n in (1, 3)]

		self.assertListEqual(
			output,
			expected,
			"Mauvaises valeurs maximales."
		)

	def test_get_sum_values_from_key(self):
		
		values = [
			{
				"money": 12,
				"problems": 14,
				"trivago": 1
			},
			{
				"money": 56,
				"problems": 406,
			},
			{
				"money": 1,
				"chichis": 1,
				"power-level": 9000
			}
		]
		expected = [
			420,
			69
		]
		output = [exercice.get_sum_values_from_key(values, k) for k in ("problems", "money")]

		self.assertListEqual(
			output,
			expected,
			"Mauvaises sommes."
		)

if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
