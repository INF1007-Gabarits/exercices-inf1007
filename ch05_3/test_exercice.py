#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
	def test_get_num_letters(self):
		values = [
			"aaa",
			"AAA",
			"aA0",
			"aA-",
			"aA ",
			"àAé"
		]
		expected = [
			3,
			3,
			3,
			2,
			2,
			3
		]
		output = [exercice.get_num_letters(v) for v in values]
		self.assertEqual(
			expected,
			output,
			"Mauvais compte de lettres"
		)

	def test_get_word_length_histogram(self):
		values = [
			"a aa-aa \t aa9  "
		]
		expected = [
			[0, 1, 0, 1, 1]
		]
		output = [exercice.get_word_length_histogram(v) for v in values]

		self.assertListEqual(
			output,
			expected,
			"Mauvais histogramme"
		)

	def test_format_histogram(self):
		values = [
			"Stop right there criminal scum! shouted the guard confidently."
		]
		expected = [
			" 1 "    "\n" \
			" 2 "    "\n" \
			" 3 *"   "\n" \
			" 4 **"  "\n" \
			" 5 ***" "\n" \
			" 6 "    "\n" \
			" 7 *"   "\n" \
			" 8 *"   "\n" \
			" 9 "    "\n" \
			"10 "    "\n" \
			"11 *"   "\n"
		]
		output = [exercice.format_histogram(exercice.get_word_length_histogram(v)).strip("\n") for v in values]

		for out, exp in zip(output, expected):
			self.is_same_formatting(out, exp)

	def test_format_horizontal_histogram(self):
		values = [
			"Stop right there criminal scum! shouted the guard confidently."
		]
		expected = [
			"    |       " "\n" \
			"   ||       " "\n" \
			"  ||| ||  | " "\n" \
			"¯¯¯¯¯¯¯¯¯¯¯¯" "\n" \
		]
		output = [exercice.format_horizontal_histogram(exercice.get_word_length_histogram(v)).strip("\n") for v in values]

		for out, exp in zip(output, expected):
			self.is_same_formatting(out, exp)

	def is_same_formatting(self, v1, v2):
		v1_lines = v1.strip("\n").split("\n")
		v2_lines = v2.strip("\n").split("\n")
		self.assertEqual(
			len(v1_lines),
			len(v2_lines),
			"Pas même nombre de lignes"
		)
		for l1, l2 in zip(v1_lines, v2_lines):
			self.assertEqual(
				l1.rstrip(),
				l2.rstrip(),
				"Ligne pas pareille"
			)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
