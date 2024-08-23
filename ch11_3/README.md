# Opérations matricielles (chapitre 11)

Nous allons ajouter les opérateurs à une classe de matrice.

## Format des données

On veut des matrices numériques dont les données sont stockées en tableau 1D en format rangée-major.

Par exemple, soit la matrice :
```
11 12 13 14
21 22 23 24
31 32 33 34
```
Le tableau rangée-major aurait cette forme :
```
tab = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
```
Pour accéder à la deuxième rangée, quatrième colonne (élément de valeur 24), on ferait `tab[1*4 + 3]`

## Accès aux éléments

On veut pouvoir accéder et modifier les éléments en y accédant à l'aide d'un tuple rangée-colonne.

Exemple :
```python
foo = Matrix(2, 3)
foo[0, 0] = 69.1
foo[0, 2] = 69.2
print(foo[0, 0])
print(foo[0, 2])
print(foo.data)
```

Sortie :
```
69.1
69.2
[69.1, 0.0, 69.2, 0.0, 0.0, 0.0]
```

## Formatage

### Conversion en string
On veut un affichage où chaque rangée est sur une ligne, avec chaque élément séparé d'un espace.

Exemple:
```python
foo = Matrix(2, 3, [
	11, 12, 13,
	21, 22, 23
])
print(foo)
```

Sortie :
```
11 12 13
21 22 23
```

### Représentation officielle

On veut une string qui représente une expression pour construire l'objet.

Exemple :
```python
foo = Matrix(2, 3, [
	11, 12, 13,
	21, 22, 23
])
print(repr(foo))
```

Sortie :
```
Matrix(2, 3, [11, 12, 13, 21, 22, 23])
```

### String formatée

On veut pouvoir dir comment chaque élément doit être formaté en passant la spécification de formatage qu'on passerait à `format()`

Exemple :
```python
foo = Matrix(2, 3, [
	1.1, 1.2, 1.3,
	2.1, 2.2, 2.3
])
print(format(foo, "5.2f"))
```

Sortie :
```
 1.10  1.20  1.30
 2.10  2.20  2.30
```

## Opérations arithmétiques

### Négation

On veut l'opposée d'une matrice.

Exemple :
```python
foo = Matrix(2, 3, [
	1.1, 1.2, 1.3,
	2.1, 2.2, 2.3
])
print(-foo)
```

Sortie :
```
-1.1 -1.2 -1.3
-2.1 -2.2 -2.3
```
### Addition

On veut l'addition/soustraction matricielle (matrice + matrice).

Exemple :
```python
foo = Matrix(2, 3, [
	1.0, 1.0, 1.0,
	2.0, 2.0, 2.0
])
bar = Matrix(2, 3, [
	0.1, 0.2, 0.3,
	0.1, 0.2, 0.3
])
print(foo + bar)
print()
print(foo - bar)
```

Sortie :
```
1.1 1.2 1.3
2.1 2.2 2.3

0.9 0.8 0.7
1.9 1.8 1.7
```

### Multiplication (matricielle et scalaire)


Exemple :
```python
foo = Matrix(2, 3, [
	11, 12, 13,
	21, 22, 23
])
bar = Matrix(3, 2, [
	11, 12,
	21, 22,
	31, 32
])
print(foo * bar)
print()
print(foo * 10)
```

Sortie :
```
776.0 812.0
1406.0 1472.0

110 120 130
210 220 230
```
