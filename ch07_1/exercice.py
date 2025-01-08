#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import *

def volEllipsoide(a : float, b : float, c : float) :
    return (4/3)*math.pi * a * b * c


def dessinerBranche(branch_len, pen_size, angle):
    pass


def dessinerArbre():
    pass

# Exercice 4 - ADN
def estValide(adn : str, caracteresValides = ["a", "t", "g", "c"]) :
    estValide = True
    trouve = False

    if len(adn) != 0 :
        estValide = False
    else :
        for chaine in adn :
            if chaine not in caracteresValides and not trouve :
                estValide = False
                trouve = True

    if not trouve :
        estValide = True

    return estValide

def proportion(adnBit, wholeAdn) :
    if estValide(wholeAdn) and estValide(adnBit) and (adnBit in wholeAdn) :
        return wholeAdn.count(adnBit) / len(wholeAdn)
    else :
        print("Erreur : Les chaînes d'adn entrées ne sont pas valides.")

def saisie(question) :
    value = input(question + "\t")

    if estValide(value):
        return value

    print(f"La {type} n'est pas valide.")
    return saisie(type)

def exercice4() :
    adn = saisie("Entrez une séquence d'ADN valide.")
   #print("La chaîne entrée est valide.")
    sequencePart = input("Entrez une partie de la séquence '" + adn + "' pour obtenir sa proportion.")
    prop = proportion(sequencePart, adn)
    print("Il y a {0:.2f}% de {1}.".format(prop*100, sequencePart))


if __name__ == '__main__' :
    exercice4()