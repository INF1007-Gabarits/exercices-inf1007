# Exercices en vrac (chapitre 7)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indications contraires, vous devez retourner les résultats des fonctions, pas les afficher directement. Vous devez, pour chaque exercice, choisir les paramètres appropriés.

## 1. Nombres de Fibonacci (nombre unique)
### `get_fibonacci_number`

Écrivez une fonction qui calculent le nombre de Fibonacci pour un index donné (index partent à 0). La définition récursive de la suite de Fibonacci est :

*F*<sub>0</sub> = 0 <br>
*F*<sub>1</sub> = 1 <br>
*F*<sub>*i*</sub> = *F*<sub>*i* - 1</sub> + *F*<sub>*i* - 2</sub>

Faites le tout en une seule instruction `return` (donc nécessairement de façon récursive)

Exemple :
```python
print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
print([get_fibonacci_number(i) for i in range(10)])
```
Résultat :
```
[0, 1, 1]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 2. Nombres de Fibonacci (séquence entière)
### `get_fibonacci_sequence`

Écrivez une fonction qui retourne la séquence de Fibonacci d'une taille donnée (donc taille 2 veut dire 2 éléments). N'utilisez pas la fonction du numéro 1 pour générer les nombres

Exemple :
```python
print(get_fibonacci_sequence(1))
print(get_fibonacci_sequence(2))
print(get_fibonacci_sequence(10))
```
Résultat :
```
[0]
[0, 1]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 3. Trier un dictionnaire par les décimales des valeurs
### `get_sorted_dict_by_decimals`

Écrivez une fonction qui retourne un dictionnaire trié en ordre croissant de la partie décimales des valeurs. Par partie décimale, on veut dire que par exemple 0.9 est plus grand que 0.42, donc tout simplement une comparaison avec la partie entière enlevée.

Faites le tout sur une seule ligne en utilisant la fonction `sorted` de Python.

Exemple :
```python
spam = {
	2: 2.1,
	3: 3.3,
	1: 1.4,
	4: 4.2
}
eggs = {
	"foo": 42.6942,
	"bar": 42.9000,
	"qux": 69.4269,
	"yeet": 420.1337
}
print(get_sorted_dict_by_decimals(spam))
print(get_sorted_dict_by_decimals(eggs))
```
Résultat :
```
{2: 2.1, 4: 4.2, 3: 3.3, 1: 1.4}
{'yeet': 420.1337, 'qux': 69.4269, 'foo': 42.6942, 'bar': 42.9}
```

## 4. Nombres de Fibonacci (générateur)
### `fibonacci_numbers`

Créez une fonction génératrice (un générateur) de nombres de Fibonacci. Contrairement au numéro 2, vous ne devez pas retourner une liste de la séquence au complet, mais plutôt générer les nombres à mesure à l'aide de `yield`. Vous ne devez pas garder en mémoire toute la série, mais seulement les éléments nécessaires, donc les deux derniers à tout moment.

Exemple :
```python
for fibo_num in fibonacci_numbers(10):
    print(fibo_num, end=" ")
```
Résultat :
```
0 1 1 2 3 5 8 13 21 34 
```

## 5. Générateur de séries récursives génériques
### `build_recursive_sequence_generator`

Écrivez une fonction qui retourne un générateur de nombres à l'aide d'une définition récursive et qui s'utilise de la même façon que le `fibonacci_numbers` du numéro précédent. La fonction prend en paramètre les valeurs initiales de la suite sous forme de liste, une fonction qui représente la définition récursive de la série et un booléen disant si toute la séquence doit être gardée en mémoire (`False` par défaut). Cette fonction prend en paramètre la liste des derniers éléments de la série.

Par exemple pour créer le générateur de Fibonacci, on devrait faire :
```python
def fibo_def(last_elems):
    return last_elems[-1] + last_elems[-2]
fibo = build_recursive_sequence_generator([0, 1], fibo_def)
for fi in fibo(10):
    print(fi, end=" ")
```
Résultat :
```
0 1 1 2 3 5 8 13 21 34 
```

## 6. Créer des générateurs

À l'aide de la fonction du numéro 5, créer des générateurs pour les séries de Lucas, de Perrin et de Hofstadter-Q. Faites chaque création de générateur sur une seule ligne en utilisant des lambda comme deuxième paramètre.

Définition de Lucas : https://en.wikipedia.org/wiki/Lucas_number#Definition <br>
Définition de Perrin : https://en.wikipedia.org/wiki/Perrin_number <br>
Définition de Hofstadter-Q : https://en.wikipedia.org/wiki/Hofstadter_sequence#Hofstadter_Q_sequence

Exemple:
```python
lucas = build_recursive_sequence_generator(TODO)
print(f"Lucas : {[elem for elem in lucas(10)]}")
perrin = build_recursive_sequence_generator(TODO)
print(f"Perrin : {[elem for elem in perrin(10)]}")
hofstadter_q = build_recursive_sequence_generator(TODO)
print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
```
Résultat :
```
Lucas : [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
Perrin : [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
Hofstadter-Q : [1, 1, 2, 3, 3, 4, 5, 5, 6, 6]
```

