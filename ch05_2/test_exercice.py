#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
	def test_format_bill_total(self):
		values = [("chaise", 1, 399.99), ("g-fuel", 3, 35.99)]
		output = exercice.format_bill_total(values)
		expected = "SOUS TOTAL     507.96 $" "\n" \
		           "TAXES           76.19 $" "\n" \
		           "TOTAL          584.15 $"
		self.assertEqual(
			expected.strip(),
			output.strip(),
			"Mauvais total de facture"
		)

	def test_format_bill_items(self):
		values = [
			("chaise ergonomique", 1, 399.99),
			("g-fuel", 69, 35.99),
			("blue screen", 2, 39.99)
		]
		output = exercice.format_bill_items(values)
		expected = (
			"chaise ergonomique     399.99 $" "\n"
			"g-fuel                2483.31 $" "\n"
			"blue screen             79.98 $"
		)
		self.assertEqual(
			expected.strip(),
			output.strip(),
			"Mauvais total de facture"
		)

	def test_format_number(self):
		values = [
			100.1114,
			-100.1114,
			1000.1116,
			-4206942.1337
		]
		expected = [
			"100.111",
			"-100.111",
			"1 000.112",
			"-4 206 942.134"
		]
		output = [exercice.format_number(v, 3).strip() for v in values]

		self.assertListEqual(
			[elem.strip() for elem in expected],
			[elem.strip() for elem in output],
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
			[elem.strip() for elem in expected],
			[elem.strip() for elem in output],
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
