#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
	def test_get_bill(self):
		values = ("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 3, 35.99)])
		output = exercice.get_bill(values[0], values[1])
		expected = "Äpik Gämmör" "\n" \
		           "SOUS TOTAL     507.96 $" "\n" \
		           "TAXES           76.19 $" "\n" \
		           "TOTAL          584.15 $"
		self.assertEqual(
			expected,
			output.strip(),
			"Mauvaise facture"
		)

	def test_format_number(self):
		values = [
			100.1114,
			-100.1114,
			1000.1115
			-4206942.1337
		]
		expected = ["{:_.3f}".format(v).replace("_", " ") for v in values]
		output = [exercice.format_number(v, 3).strip() for v in values]

		self.assertListEqual(
			output,
			expected,
			"Mauvais formatage"
		)

	def test_get_triangle(self):
		values = [
			1,
			2,
			5
		]
		expected = [
			"+++" "\n"
			"+A+" "\n"
			"+++",
			"+++++" "\n"
			"+ A +" "\n"
			"+AAA+" "\n"
			"+++++",
			"+++++++++++" "\n"
			"+    A    +" "\n"
			"+   AAA   +" "\n"
			"+  AAAAA  +" "\n"
			"+ AAAAAAA +" "\n"
			"+AAAAAAAAA+" "\n"
			"+++++++++++"
		]
		output = [exercice.get_triangle(v).strip() for v in values]
		
		self.assertListEqual(
			output,
			expected,
			"Mauvais triangle"
		)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
