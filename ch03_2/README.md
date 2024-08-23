# Exercices du chapitre 3

Chaque exercice est dans une fonction dans [exercice.py](exercice.py) et retourne le résultat.

## 1. Puissance

Écrire un algorithme qui calcule la puissance dissipée par une résistance selon la formule _P = V² / R_

## 2. Vecteurs orthogonaux

Écrire un algorithme qui détermine si deux vecteurs à deux dimensions sont orthogonaux ou non. Note : utiliser un produit scalaire, les opérations sur les vecteurs, dont le produit scalaire, ne sont pas des opérations élémentaires disponibles pour l'exercice. Acceptons l'hypothèse qu'un vecteur nul est orthogonal à n'importe quel autre vecteur.

## 3. Moyenne d'une liste

Écrire un algorithme qui calcule la moyenne entre des valeurs positives d'une liste. Le nombre de valeurs n’est pas connu à l’avance, et il faut ignorer les valeurs négatives.

Par exemple, la liste [1, 4, -2, 10] donne une moyenne de 5.

## 4. Monnaie à rendre

Écrire un algorithme qui calcule, à partir d'une valeur entière, la monnaie à rendre en billets de 20$, 10$, 5$ et en pièces de 1$.

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
