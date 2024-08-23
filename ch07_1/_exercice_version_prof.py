#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys
sys.path.insert(1, 'D:\charge_cours\INF1007\H2021\exercices\\2021H_ch6_1_exercices')
from exercice_ch6 import frequence
from turtle import *
import re

def compute_volume_and_mass(a=2, b=4, c=6, masse_vol=10):
    volume = math.pi * a * b * c * 4 / 3
    masse = volume * masse_vol

    return volume, masse

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def draw_tree():
    setheading(90)
    color("green")
    draw_branch(70, 7, 35)
    done()


def valide(saisie):
    """
    if len(saisie) != 0:
        return set(saisie).issubset("atgc")

    return False
    """

    return bool(re.match("^[atgc]+$", saisie))


def saisie(type):
    value = input(f"Entrez une {type} d'ADN valide: ")

    if valide(value):
        return value

    print(f"La {type} n'est pas valide")
    return saisie(type)


def proportion(chain, sequence):

    return chain.count(sequence) / len(chain)


def check_dna():
    chain = saisie("chaine")
    sequence = saisie("sequence")

    prop = proportion(chain, sequence)
    print("Il y a {0:.2f} % de {1}.".format(prop*100, sequence))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    draw_tree()
    print(compute_volume_and_mass())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("big big test bb"))
    check_dna()

