#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import inspect

from exercice import *


class TestExercice(unittest.TestCase):
	def test_its_all_good(self):
		self.assertTrue(True)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
