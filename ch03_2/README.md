# Exercices du chapitre 3

Chaque exercice est dans une fonction dans [exercice.py](exercice.py) et retourne le résultat.

## 1. Puissance

Écrire un algorithme qui calcule la puissance dissipée par une résistance selon la formule _P = V² / R_

## 2. Vecteurs orthogonaux

Écrire un algorithme qui détermine si deux vecteurs à deux dimensions sont orthogonaux ou non. On note que les opérations sur les vecteurs, dont le produit scalaire, ne sont pas des opérations élémentaires disponibles pour l'exercice, il faut donc les écrire nous-mêmes. Acceptons l'hypothèse qu'un vecteur nul est orthogonal à n'importe quel autre vecteur.

## 3. Point à l'intérieur d'un cercle

Soit un cercle défini par un centre (vecteur 2D) et un rayon, ainsi qu'un point (vecteur 2D). Écrire un algorithme qui détermine si le point est à l'intérieur du cercle.

## 4. Monnaie à rendre

Écrire un algorithme qui calcule, à partir d'une valeur réelles, la monnaie à rendre en billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢. Depuis 2013, la pièce de une cent (la _cenne noire_) n'est plus en distribution au Canada, on doit donc arrondir au multiple de 0.05$ le plus proche (donc à la pièce de 5¢ près).

## 5. Formater dans une base numérique donnée

Écrire un algorithme qui permet de formater un nombre donné dans une base donné en utilisant une séquence de lettres données pour représenter les chiffres. Par exemple, formater 123 en base 16 nous donne 7B, et il faut donc fournir les chiffres hexadécimaux, donc 0123456789ABCDEF.

Exemple d'utilisation : 
```python
  print(format_base(123, 10, "0123456789"))
  print(format_base(123, 16, "0123456789ABCDEF"))
  print(format_base(12, 2, "01"))
```
Nous donne
```
  123
  7B
  1100
```
