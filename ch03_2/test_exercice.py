#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

from exercice import *


class TestExercice(unittest.TestCase):
	def setUp(self):
		pass

	def test_dissipated_power(self):
		data = [
			(69, 420),
			(42, 9000)
		]
		expected = [
			69*69/420,
			42*42/9000
		]
		output = [dissipated_power(*d) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)

	def test_orthogonal(self):
		data = [
			((1, 1), (-1, 1)),
			((0, 0), (1, 1)),
			((0, 0), (0, 0)),
			((1, 1), (1, 1)),
			((-1, -1), (1, 1))
		]
		expected = [
			True,
			True,
			True,
			False,
			False
		]
		output = [orthogonal(d[0], d[1]) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)

	def test_point_in_circle(self):
		data = [
			((0, 0), (1, 0), 2),
			((0, 0), (1, 0), 1),
			((0, 0), (1, 1), 1),
			((-1, 0), (1, 0), 2),
			((-1, 1), (1, 1), 2),
			((-1, -1), (1, 1), 2),
			((-1, -1), (1, 1), 3),
		]
		expected = [
			True,
			True,
			False,
			True,
			True,
			False,
			True,
		]
		output = [point_in_circle(d[0], d[1], d[2]) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)

	def test_cash(self):
		data = [
			0,
			1,
			5,
			10,
			20,
			420,
			69,
			137,
			0xBABE,
			0.05,
			0.10,
			0.25,
			0.15,
			0.35,
			0.40,
			0.20,
			0.50,
			0.55,
			0.12,
			0.13,
			1337.88
		]
		expected = [
			(   0, 0, 0, 0, 0, 0, 0),
			(   0, 0, 0, 1, 0, 0, 0),
			(   0, 0, 1, 0, 0, 0, 0),
			(   0, 1, 0, 0, 0, 0, 0),
			(   1, 0, 0, 0, 0, 0, 0),
			(  21, 0, 0, 0, 0, 0, 0),
			(   3, 0, 1, 4, 0, 0, 0),
			(   6, 1, 1, 2, 0, 0, 0),
			(2390, 0, 1, 1, 0, 0, 0),
			(   0, 0, 0, 0, 0, 0, 1),
			(   0, 0, 0, 0, 0, 1, 0),
			(   0, 0, 0, 0, 1, 0, 0),
			(   0, 0, 0, 0, 0, 1, 1),
			(   0, 0, 0, 0, 1, 1, 0),
			(   0, 0, 0, 0, 1, 1, 1),
			(   0, 0, 0, 0, 0, 2, 0),
			(   0, 0, 0, 0, 2, 0, 0),
			(   0, 0, 0, 0, 2, 0, 1),
			(   0, 0, 0, 0, 0, 1, 0),
			(   0, 0, 0, 0, 0, 1, 1),
			(  66, 1, 1, 2, 3, 1, 1),
		]
		output = [cash(d) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)

	def test_format_base(self):
		digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		data = [
			(123, 10, digits),
			(123, 16, digits),
			(123, 2, digits),
			(123, 8, digits),
			(123, 11, digits),
			(-123, 16, digits),
			(-123, 20, digits)
		]
		expected = [
			"123",
			"7B",
			"1111011",
			"173",
			"102",
			"-7B",
			"-63"
		]
		output = [format_base(*d) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)



if __name__ == "__main__":
	if not os.path.exists("logs"):
		os.mkdir("logs")
	with open("logs/tests_results.txt", "w") as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	# Pour mettre le résultat du log dans la console (plus pratique).
	print(open("logs/tests_results.txt", "r").read())
