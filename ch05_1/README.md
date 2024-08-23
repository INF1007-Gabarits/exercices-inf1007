[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 5)

Avant de commencer, consultez les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Écrire un programme qui lit un nombre et affiche sa valeur absolue, sans utiliser de fonction avancée
2. Dans un conte américain, huit petits canetons s'appellent respectivement : Jack, Kack, Lack, Mack, Nack, Oack, Pack et Qack. Écrire un petit script qui génère tous ces noms à partir des deux chaînes suivantes : prefixes = 'JKLMNOPQ' et suffixe = 'ack'
3. Calculer la somme des 100 premiers nombres entiers premiers excluant le nombre 1
4. Calculer la factorielle d’un nombre entier, sans utiliser de fonction avancée
5. Utiliser l’instruction 'continue' pour modifier une boucle for d’affichage de tous les entiers de 1 à 10 compris, sauf lorsque la variable de boucle vaut 5
6. Vérifier si un groupe est acceptable selon l'âge de plusieurs personnes faisant partie de plusieurs groupes. Vous devez retourner une liste booléenne. Les conditions d'acceptation sont les suivantes:
    - Critère de taille: Si le groupe possède plus que 10 membres ou 3 membres et moins, il n'est pas acceptable
    - Critère d'âge: Si au moins un membre du groupe est mineur, le groupe n'est pas acceptable
    - Critère d'âge: Si un membre du groupe est plus vieux que 70 ans et qu'un autre membre du groupe à exactement 50 ans, le groupe n'est pas acceptable
    - Critère d'âge: Si au moins un membre du groupe à exactement 25 ans, alors le groupe est acceptable peut-importe les autres critères d'âges

### À compléter
Vous devez compléter les fonctions suivantes du fichier [exercice.py](exercice.py).

```python
def convert_to_absolute(number: float) -> float:
    return 0


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [""]


def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []
```
