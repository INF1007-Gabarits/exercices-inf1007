[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 6)

Avant de commencer, consultez les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Écrire un programme qui transforme une liste en dictionnaire. Les éléments de la liste deviennent les clés du dictionnaire et les indexes de chaque élément deviennent la valeur associée à chaque clé.
2. Écrire un programme qui trouve la valeur hex de chaque couleur d'une liste et crée une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex.
3. Écrire un programme qui crée une listes des 10 000 premiers entiers positif (0 inclu), sauf pour les entiers de 15 à 350.
4. Écrire un programme qui calcule l'erreur quadratique moyen pour différents modèles AI. Un dictionnaire des résultats de chaque modèle est passé en paramètre. Pour chaque modèle, une liste contenant des tuples (valeur_réelle, valeur_prédite) est fournie.

### À compléter
Vous devez compléter les fonctions suivantes du fichier [exercice.py](exercice.py).

```python
def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    
    return {}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex

    return []


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350

    return []
    
def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.

    return {}
```
