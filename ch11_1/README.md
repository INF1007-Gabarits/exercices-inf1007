
# Combat de personnages dans un jeu (chapitre 11)

<!-- Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md) -->

Nous allons programmer une classe de personnage très simple qui permet d'effectuer des combats tour-à-tour dans un jeu.

## Armes des personnages (`character.Weapon`)

On veut une classe qui représente une arme. Une arme possède un nom, un niveau d'attaque et un niveau de personnage minimal pour l'utiliser.

Le nom ne peut pas être changé.

On a une méthode `compute_damage` qui calcule les dégâts infligés par un personnage utilisant l'arme à un autre personnage (en paramètres). La formule est la suivante : 

<img src="doc/assets/dmg_eq.png" width="600">

Où *a* est l'attaquant et *d* est le défendeur. <br>
*crit* est égal à 2 environ 1/16 (6.25%) du temps, 1 sinon <br>
*random* est un nombre réel aléatoire entre 85% et 100%

Cette formule est implémentée dans la fonction globale `utils.compute_damage_output` à laquelle on peut passer les différentes constantes de la formule comme la probabilité de coup critique.

On a une méthode `is_usable_by` qui prend un personnage en paramètre et retourne vrai si le personnage peut utiliser l'arme (son niveau est >= au `min_level` de l'arme).

On a une méthode `use` qui prend un utilisateur de l'arme et un adversaire. Elle calcule le dommage et l'applique au `hp` de l'opposant, puis retourne un message disant le dommage appliqué.

On veut une méthode de classe `make_unarmed` qui construit un `Weapon` nommé `"Unarmed"` avec une puissance de 20.

## Personnages du jeu (`character.Character`)

Dans notre jeu, un personnage est composé des propriétés suivantes :

`Character.name` : Le nom du personnage <br>
`Character.max_hp` : HP maximum <br>
`Character.attack` : Le niveau d'attaque du personnage <br>
`Character.defense` : Le niveau de défense du personnage <br>
`Character.level` : Le niveau d'expérience du personnage <br>
`Character.weapon` : L'arme utilisée par le personnage <br>
`Character.hp` : Les HP restants <br>

Le nom ne peut pas être changé publiquement après l'initialisation.

Le HP doit toujours rester dans l'intervalle [0, `max_hp`]

Un changement au `max_hp` doit doit aussi changer le `hp` pour rester dans l'intervalle valide.

Affecter `None` comme arme doit construire un *unarmed* en utilisant le `Weapon.make_unarmed`. Affecter une arme à un personnage qui n'a pas le niveau suffisant lève un `ValueError`.

La méthode `apply_turn` utilise l'arme du personnage (en appelant `Weapon.use`) à un adversaire passé en paramètre et retourne le message. Par exemple :

```python
c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)
c1.weapon = Weapon("BFG", 100, 69)
print(c1.apply_turn(c2))
```
Pourrait donner la sortie:
```
Äpik used BFG
Critical hit! Gämmor took 132 dmg
```

## Déroulement d'un combat (`game.run_battle`)

La fonction prend en paramètre le personnage attaquant et le personnage défendeur (dans cet ordre) et exécute les attaques entre les personnages, tour-à-tour, jusqu'à ce qu'un des deux meurt (HP à zéro). La fonction retourne le nombre total de tours effectués.

C'est la méthode `Character.apply_turn` qui applique le dommage et qui nous donne le message à afficher à chaque tour.

Exemple :
```python
c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

turns = run_battle(c1, c2)
print(f"The battle ended in {turns} turns.")
```

Sortie :
```
Äpik starts a battle with Gämmör!

Äpik used BFG
Gämmör took 70 dmg

Gämmör used Deku Stick
Äpik took 80 dmg

Äpik used BFG
Gämmör took 71 dmg

Gämmör used Deku Stick
Critical hit! Äpik took 178 dmg

Äpik is sleeping with the fishes.
The battle ended in 4 turns.
```
