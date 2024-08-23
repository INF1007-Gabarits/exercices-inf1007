[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 6)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indications contraires, vous devez retourner les résultats des fonctions, pas les afficher directement. Vous devez au possible faire les numéros en une seule instruction `return` (à moins d'avis contraire).

## 1. Clés paires d'un dictionnaire
### `get_even_keys`

Extrayez sous forme d'ensemble (`set`) les clés paires d'un dictionnaire.

Exemple :
```python
yeet = {
    69: "Yeet",
    420: "YeEt",
    9000: "YEET"
}
print(get_even_keys(yeet))
```
Résultat :
```
{9000, 420}
```
## 2. Concaténation de dictionnaires
### `join_dictionaries`

Concaténez une liste de dictionnaires en un seul dictionnaire.

Exemple :
```python
yeet = {
    69: "Yeet",
    420: "YeEt",
    9000: "YEET"
}
doot = {
    0xBEEF: "doot",
    0xDEAD: "DOOT",
    0xBABE: "dOoT"
}
print(join_dictionaries([yeet, doot]))
```
Résultat :
```
{69: 'Yeet', 420: 'YeEt', 9000: 'YEET', 48879: 'doot', 57005: 'DOOT', 47806: 'dOoT'}
```

## 3. Dictionnaire à partir de listes
### `dictionary_from_lists`

Générez un dictionnaire à partir de deux listes, une de clés et une de valeurs. Votre dictionnaire devrait avoir autant d'éléments que la plus petite des deux listes.

Exemple :
```python
doh = [
    "D'OH!",
    "d'oh",
    "DOH!"
]
nice = [
    "NICE!",
    "nice",
    "nIcE",
    "NAIIIIICE!"
]
print(dictionary_from_lists(doh, nice))
```
Résultat :
```
{"D'OH!": 'NICE!', "d'oh": 'nice', 'DOH!': 'nIcE'}
```

## 4. Plus grandes valeurs d'un dictionnaire
### `get_greatest_values`

Trouvez les *n* (2e paramètre) plus grandes valeurs d'un dictionnaire. Il faut les retourner sous forme d'une liste décroissante.

Exemple :
```python
nums = {
    "nice": 69,
    "nice bro": 69420,
    "AGH!": 9000,
    "dude": 420,
    "git gud": 1337
}
print(get_greatest_values(nums, 1))
print(get_greatest_values(nums, 3))
```
Résultat :
```
[69420]
[69420, 9000, 1337]
```

## 5. Somme des valeurs dans une liste de dictionnaires
### `get_sum_values_from_key`

Calculez la somme des valeurs d'une clé donnée dans une liste de dictionnaires.

Exemple :
```python
bro1 = {
    "money": 12,
    "problems": 14,
    "trivago": 1
}
bro2 = {
    "money": 56,
    "problems": 406
}
bro3 = {
    "money": 1,
    "chichis": 1,
    "power-level": 9000
}
print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
print(get_sum_values_from_key([bro1, bro2, bro3], "money"))

```
Résultat :
```
420
69
```
