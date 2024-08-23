[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 6)

Avant de commencer, consultez les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Écrire un programme qui demande à l’utilisateur d’entrer 10 valeurs (entier, float, str), et qui ordonne la liste fournie.
2. Deux mots sont des anagrammes si vous pouvez réarranger les lettres de l'un pour en former l'autre (par exemple ALEVIN et NIVELA sont des anagrammes). Écrivez un programme qui demande deux chaînes de caractère et qui vérifie si ce sont des anagrammes.
3. Écrire un programme qui vérifie si une liste contient des doublons, c’est-à-dire si la liste ne contient que des éléments uniques.
4. Écrire un programme qui calcule la moyenne des notes rentrées dans un dictionnaire ayant pour clés le nom des étudiants. Par la suite, le programme doit retourner le nom de l’étudiant ayant la meilleure note, dans la même structure de données.
5. À partir d’une phrase donnée par l’utilisateur, écrire un programme qui affiche toutes les lettres qui sont utilisées plus de 5 fois dans la phrase, en ordre décroissant d’utilisation (le plus fréquent en premier).
6. Écrire un programme qui permet de sauvegarder les ingrédients nécessaires à plusieurs recettes, dans une seule structure de données. Par la suite, écrire un programme qui affiche les ingrédients d’une recette, en vérifiant au préalable si cette recette est dans notre livre de recettes.

### À compléter
Vous devez compléter les fonctions suivantes du fichier [exercice.py](exercice.py).

```python
def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        pass

    return []

def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        pass

    return False

def contains_doubles(items: list) -> bool:
    return False

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données 
    pass

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass
```
