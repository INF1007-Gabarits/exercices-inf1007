[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 3)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Calculer la racine carré et le carré d'un nombre
2. Calculer la moyenne de 3 nombres donnés
3. Convertir en radians un angle fourni au départ en degrés, minutes, secondes
4. Convertir en degrés, minutes, secondes un angle fourni au départ en radians
5. Convertir en degrés Celsius une température exprimée au départ en degrés Fahrenheit et vice-versa

### À compléter
Vous devez compléter les fonctions suivantes du fichier [exercice.py](exercice.py).

```python
def square_root(a: float) -> float:
    return 0.0

def square(a: float) -> float:
    return 0.0

def average(a: float, b: float, c: float) -> float:
    return 0.0

def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return 0.0

def to_degrees(angle_rads: float) -> tuple:
    return 0.0, 0.0, 0.0

def to_celsius(temperature: float) -> float:
    return 0.0

def to_farenheit(temperature: float) -> float:
    return 0.0
```

## Connaissances utiles

### Opérateurs arithmétiques de base
https://www.w3schools.com/python/python_operators.asp

### Documentation du module math
https://docs.python.org/3/library/math.html

### Formule de conversion Celsius vers Farenheit
Tf = Tc x 1.8 + 32
