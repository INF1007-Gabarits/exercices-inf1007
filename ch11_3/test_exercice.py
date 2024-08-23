#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from unittest import mock
import inspect

from _matrix_version_prof import *


class TestMatrix(unittest.TestCase):
	def setUp(self):
		self.d22 = [
			11, 12,
			21, 22
		]
		self.d23 = [
			11, 12, 13,
			21, 22, 23
		]
		self.d32 = [
			11, 12,
			21, 22,
			31, 32
			
		]
		self.d45 = [
			11, 12, 13, 14, 15,
			21, 22, 23, 24, 25,
			31, 32, 33, 34, 35,
			41, 42, 43, 44, 45,
		]

	def test_properties(self):
		m23 = Matrix(2, 3, self.d23)
		with self.assertRaises(AttributeError):
			m23.height = 2
		with self.assertRaises(AttributeError):
			m23.width = 2
		with self.assertRaises(AttributeError):
			m23.data = self.d23

	def test_init_valid(self):
		m23 = Matrix(2, 3, self.d23)
		self.assertEqual(m23.height, 2)
		self.assertEqual(m23.width, 3)
		self.assertIs(m23.data, self.d23)
		m22 = Matrix(2, 2)
		self.assertListEqual(m22.data, [0.0, 0.0, 0.0, 0.0])
		m22 = Matrix(2, 2, 1.0)
		self.assertListEqual(m22.data, [1.0, 1.0, 1.0, 1.0])

	def test_init_invalid(self):
		with self.assertRaises(DimensionsTypeError):
			m = Matrix(1.1, 1)
		with self.assertRaises(DimensionsTypeError):
			m = Matrix(1, 1.1)
		with self.assertRaises(DimensionsError):
			m = Matrix(0, 1)
		with self.assertRaises(DimensionsError):
			m = Matrix(1, 0)
		with self.assertRaises(DataSizeError):
			m = Matrix(2, 2, self.d23)
		with self.assertRaises(DataTypeError):
			m = Matrix(2, 2, "henlo")

	def test_get_valid(self):
		m45 = Matrix(4, 5, self.d45)
		self.assertEqual(m45[0, 0], self.d45[0])
		self.assertEqual(m45[0, 4], self.d45[4])
		self.assertEqual(m45[2, 0], self.d45[10])
		self.assertEqual(m45[2, 4], self.d45[14])

	def test_set_valid(self):
		m45 = Matrix(4, 5)
		m45[0, 0] = 69.1
		m45[0, 3] = 69.2
		m45[2, 0] = 69.3
		m45[2, 4] = 69.4
		self.assertEqual(m45[0, 0], 69.1)
		self.assertEqual(m45[0, 3], 69.2)
		self.assertEqual(m45[2, 0], 69.3)
		self.assertEqual(m45[2, 4], 69.4)

	def test_add_valid(self):
		data1 = Matrix(2, 3, [11, 12, 13, 21, 22, 23])
		data2 = Matrix(2, 3, [1100, 1200, 1300, 2100, 2200, 2300])
		expected = Matrix(2, 3, [1111, 1212, 1313, 2121, 2222, 2323])
		output = data1 + data2
		self.assertEqual(output, expected)

	def test_mul_valid(self):
		data1 = Matrix(2, 3, self.d23)
		data2 = Matrix(3, 2, self.d32)
		expected = Matrix(2, 2, [
			 776,  812,
			1406, 1472
		])
		output = data1 * data2
		self.assertEqual(output, expected)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
