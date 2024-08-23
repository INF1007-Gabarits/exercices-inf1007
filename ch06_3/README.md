[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 6)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indications contraires, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Maximums d'une liste de listes
### `get_maximums`

Générez la liste des maximums d'une liste de listes de nombres. On veut donc le maximum de chacune des listes.

Exemple :
```python
print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
```
Résultat :
```
[3, 6, 12, 9]
```
## 2. Concaténation de nombres
### `join_integers`

Concaténez une liste d'entiers naturels en un seul nombre. Le type retourné doit être un entier, pas une string, et la fonction doit être faite en une seule expression (une seule ligne qui est le `return`). Vous pouvez faire des conversions de string/entiers.

Exemple :
```python
print(join_integers([111, 222, 333]))
print(join_integers([69, 420]))
```
Résultat :
```
111222333
69420
```

## 3. Crible d'Ératosthène
### `generate_prime_numbers`

Générez la liste des nombres premiers jusqu'à un certain nombre en suivant le crible d'Ératosthène (https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne). Voici l'agorithme en pseudo-code :
```
FONCTION Eratosthène(limite)
    premiers = liste vide
    nombres = liste des entiers de 2 à limite
    TANT QUE nombres est non vide FAIRE
        Ajouter à premiers le premier entier de nombres
        nombres = liste des entiers de nombres non multiples du premier
    RÉSULTAT premiers
```

Exemple :
```python
print(generate_prime_numbers(17))
```
Résultat :
```
[2, 3, 5, 7, 11, 13, 17]
```

Notez que la borne supérieure (si elle première) est incluse dans le résultat.

## 4. Combinaisons de strings et de nombres
### `combine_strings_and_numbers`

Générez une liste en concaténant les éléments d'une liste de string (1er param) et les nombres de 1 à n (2e param). Vous devez exclure les multiples d'un certain nombre (3e param). Si ce troisième paramètre est `None`, alors on n'exclut rien.

Exemple:
```python
print(combine_strings_and_numbers(["A", "B"], 2, None))
print(combine_strings_and_numbers(["A", "B"], 5, 2))
```
Résultat :
```
['A1', 'B1', 'A2', 'B2']
['A1', 'B1', 'A3', 'B3', 'A5', 'B5']
```

Notez que dans le deuxième exemple la valeur 5 est incluse et que les multiples de 2 (2 et 4) sont exclus. Notez aussi l'ordre A1 B1 puis A2 B2. On génère toutes les combinaisons pour un nombre avant de passé au prochain. On ne veut pas A1 A2 puis B1 B2.

## Conseils et ressources

`len()` : https://docs.python.org/3/library/functions.html?highlight=len#len

`str.join()` : https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join

`max()` : https://docs.python.org/3/library/functions.html?highlight=max#max
