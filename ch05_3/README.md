[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Histogrammes de longueur de mots (chapitre 5)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indications contraires, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Nombre de lettres d'un mot
### `get_num_letters`

Compter le nombre de caractères alphanumériques d'une string. Vous ne devez pas compter la ponctuation comme étant une lettre du mot. Donc si un mot contient des caractères de ponctuation (trait d’union, apostrophe, point, virgule, etc.), vous devez y soustraire ceux-ci dans le nombre de lettres du mot. Par exemple, le mot «est?» contient trois lettres et le mot «[reus]» en contient quatre. Utilisez `isalnum` pour déterminer si un caractère est alphanumérique ou non.

## 2. Histogramme de longueurs de mots
### `get_word_length_histogram`

Construire un histogramme du nombre de lettres des mots d'un texte. Vous devez retourner une liste où l'élément à un index donné est le nombre de mots ayant un nombre de lettres égal à cet index. Par exemple, l'histogramme `[0, 3, 0, 2]` représente un texte qui a trois mots d'une lettre, aucun mots de deux lettres et deux mots de trois lettres. Le premier élément de la liste (le compte de mots à zéro lettre) devrait toujours être égal à 0.

Par exemple :
```python
spam = "Stop right there criminal scum! shouted the guard confidently."
eggs = get_word_length_histogram(spam)
print(eggs)
```
donne la sortie
```
[0, 0, 0, 1, 2, 3, 0, 1, 1, 0, 0, 1]
```

## 3. Formatage d'un histogramme
### `format_histogram`

Construire une version affichable de l'histogramme où chaque élément de l'histogramme (sauf le premier élément nul) est représenté par le nombre d'occurrences de la longueur suivie d'une rangée d'étoiles de cette longueur.

Par exemple, si on reprend l'histogramme précédent :
```python
spam = format_histogram([0, 0, 0, 1, 2, 3, 0, 1, 1, 0, 0, 1])
print(spam)
```
On obtient :
```
 1
 2
 3 *
 4 **
 5 ***
 6
 7 *
 8 *
 9
10
11 *
```

Remarquez qu'on ignore la rangée 0 (qui est toujours égale à 0 et ne représente rien) et que le numéro de la rangée est aligné à droite sur exactement le bon nombre de caractères.

## 4. Histogramme à colonnes verticales
### `format_horizontal_histogram`

Afficher l'histogramme, mais avec des colonnes verticales (faites avec le caractère `BLOCK_CHAR`) et sans mettre les numéros de colonnes. Il faut aussi mettre une ligne en bas de l'histogramme (caractère `LINE_CHAR`) représentant l'axe et exactement de la même longueur que la largeur de l'histogramme.

En réutilisant encore le même histogramme :
```python
spam = format_horizontal_histogram([0, 0, 0, 1, 2, 3, 0, 1, 1, 0, 0, 1])
print(spam)
```
On obtient :
```
    |
   ||
  ||| ||  |
¯¯¯¯¯¯¯¯¯¯¯¯
```

## Conseils et ressources

`len()` : https://docs.python.org/3/library/functions.html?highlight=len#len

`str.isalpha()` : https://docs.python.org/3/library/stdtypes.html?highlight=isalpha#str.isalpha

`str.split()` : https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split

`str.join()` : https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join

`max()` : https://docs.python.org/3/library/functions.html?highlight=max#max

Spécifications des string formatées : https://docs.python.org/3/library/string.html#formatspec

Table des caractères d'échappement : https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
