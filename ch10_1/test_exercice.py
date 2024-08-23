#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import numpy as np

import exercice


class TestExercice(unittest.TestCase):
    def test_linear_values(self):
        output = list(exercice.linear_values())
        answer = list(np.linspace(start=-1.3, stop=2.5, num=64))
        self.assertListEqual(
            output,
            answer,
            'Mauvaise identification de la parité de la longueur de la chaine'
        )

    def test_coordinates(self):
        cartesian_coordinates = np.array([(0, 0), (10, 10), (2, -1)])
        
        output = exercice.coordinate_conversion(cartesian_coordinates)
        answer = np.array([(np.sqrt(c[0] ** 2 + c[1] ** 2), np.arctan2(c[1], c[0])) for c in cartesian_coordinates])

        np.testing.assert_array_equal(
            output,
            answer,
            'Mauvaise réponse'
        )

    def test_closest(self):
        values = np.array([1, 3, 8, 10])
        number = 9.5

        output = exercice.find_closest_index(values, number)
        answer = np.abs(values - number).argmin()

        self.assertEqual(
            output,
            answer,
            'Erreur dans le remplacement de caractère'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)