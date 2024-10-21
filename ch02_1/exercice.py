#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot) :
    # asciiMin - asciiMaj = 32
    dif = abs(ord('A') - ord('a')) # 32 (Nous prenons la lettre "a" en référence, mais nous aurions pu prendre une autre lettre.)

    nouvMot = ""
    for caractere in mot :
        caractere = ord(caractere)
        if (ord('a') <= caractere and caractere <= ord('z')) :
            lettreMaj = caractere - dif
            nouvMot += chr(lettreMaj)
        elif (ord('A') <= caractere and caractere <= ord('Z')) :
            lettreMin = caractere + dif
            nouvMot += chr(lettreMin)
        else :
            nouvMot += caractere

    return nouvMot

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]

    print(mots)

    for i in range(len(mots)): # for(i = 0 ; i < mots.length ; i++)
        mots[i] = majuscule(mots[i])

    print(mots)
