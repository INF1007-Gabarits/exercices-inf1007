#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def setUp(self):
        with open('./data/sample_words.txt') as f:
            self.words = [word.replace('\n', '') for word in f.readlines()]
    
    def test_upper_case_names(self):
        altered_words = [word.upper() for word in self.words]
        output = list(map(exercice.majuscule, self.words))
        self.assertListEqual(
            output,
            altered_words,
            'Toutes les lettres doivent être en majuscule.'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
    print(open('logs/tests_results.txt', 'r').read())
