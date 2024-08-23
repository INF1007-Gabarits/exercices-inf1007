#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from unittest import mock
import inspect
import random

from game import *
from character import *


class TestWeapon(unittest.TestCase):
	def setUp(self):
		self.w1 = Weapon("w1", 1, 69)
		self.w2 = Weapon("w2", 69, 1)
		self.w3 = Weapon("w3", 69, 42)
		self.w4 = Weapon.make_unarmed()

	def test_name(self):
		with self.assertRaises(AttributeError):
			self.w1.name = "henlo"

	def test_init(self):
		self.assertEqual(self.w3.name, "w3")
		self.assertEqual(self.w3.power, 69)
		self.assertEqual(self.w3.min_level, 42)

	def test_unarmed(self):
		self.assertEqual(self.w4.name, "Unarmed")
		self.assertEqual(self.w4.power, Weapon.UNARMED_POWER)
		self.assertEqual(self.w4.min_level, 1)


class TestCharacter(unittest.TestCase):
	def setUp(self):
		self.hp_only =  Character("hp_only",  69,  1,  1,  1)
		self.atk_only = Character("atk_only",  1, 69,  1,  1)
		self.def_only = Character("def_only",  1,  1, 69,  1)
		self.lvl_only = Character("lvl_only",  1,  1,  1, 69)
		self.foo = Character("foo", 101, 102, 103, 104)
		self.bar = Character("bar", 201, 202, 203, 204)
		self.wpn1 = Weapon("wpn1", 11, 12)
		self.bar.weapon = self.wpn1

	def test_name(self):
		with self.assertRaises(AttributeError):
			self.foo.name = "henlo"

	def test_weapon(self):
		self.assertEqual(self.bar.weapon.name, self.wpn1.name)
		self.bar.weapon = Weapon("wpn2", 1, 2)
		self.assertEqual(self.bar.weapon.name, "wpn2")
		self.bar.weapon = None
		self.assertEqual(self.bar.weapon.name, "Unarmed")

	def test_init(self):
		self.assertEqual(self.foo.name, "foo")
		self.assertEqual(self.foo.max_hp, 101)
		self.assertEqual(self.foo.attack, 102)
		self.assertEqual(self.foo.defense, 103)
		self.assertEqual(self.foo.level, 104)
		self.assertEqual(self.foo.hp, self.foo.max_hp)
		self.assertEqual(self.foo.weapon.name, "Unarmed")

	@mock.patch("random.random", new=lambda: 0.01)
	@mock.patch("random.uniform", new=lambda a, b: 0.01)
	def test_crit(self):
		msg = self.foo.apply_turn(self.bar)
		self.assertIn("critical", msg.lower())

	@mock.patch("random.random", new=lambda: 0.99)
	@mock.patch("random.uniform", new=lambda a, b: 0.99)
	def test_crit(self):
		msg = self.foo.apply_turn(self.bar)
		self.assertNotIn("critical", msg.lower())


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
