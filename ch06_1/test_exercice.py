#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from collections import Counter

import exercice


class TestExercice(unittest.TestCase):
    def test_order(self):
        values = [
            [1, 9, -2, 6],
            ["a", "2", "hello"]
        ]

        output = [exercice.order(v) for v in values]
        answer = [sorted(v) for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvais ordre'
        )

    def test_anagram(self):
        words = [
            ["allo", "lola"],
            ["toto", "le clown"]
        ]
        
        answer = [True, False]
        output = [exercice.anagrams(v) for v in words]

        self.assertEqual(
            output,
            answer,
            'Erreur dans la vérification de l\'anagramme'
        )

    def test_doubles(self):
        values = [
            [1, 2, 3, 4],
            [1, 1, 2, 3, 5, 8]
        ]

        output = [exercice.contains_doubles(v) for v in values]
        answer = [False, True]

        self.assertListEqual(
            output,
            answer,
            'Erreur dans les doublons'
        )

    def test_grades(self):
        value = {"Sam": [80, 90, 85], "Sei": [100, 50, 50]}


        output = exercice.best_grades(value)
        answer = {"Sam": 85}

        self.assertDictEqual(
            output,
            answer,
            'Erreur dans les notes'
        )

    def test_frequence(self):
        sentences = [
            "Bonjour, bonjour",
            "J'adore mon baccalaureat en genie informatique/logiciel"
        ]

        output = [exercice.frequence(s) for s in sentences]
        answer = [dict(Counter(s)) for s in sentences]

        self.assertListEqual(
            output,
            answer,
            'Erreur dans les histogrammes'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)