
# Magie! (chapitre 11)

<!-- Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md) -->

Nous allons reprendre  le jeu que nous avons fait précédemment en ajoutant d'autres sortes d'actions.

## Personnages (`character.Character`)

La classe a un peu changé par rapport à sa version précédente. Plutôt que d'avoir une arme, les personnages on des actions (*moves*), dont une frappe sans arme (*unarmed attack*) et deux actions quelquonques (`Character.main_move` et `Character.secondary_move`)

## Action de base (`character.Move`)

`Move` est la classe de base pour toutes les actions que les personnages peuvent effectuer. Elle définie trois propriétés : son nom (`name`), son niveau minimal (`min_level`) et son utilisateur actuel (`user`).

Elle possède aussi trois méthodes qui peuvent être surchagées pour obtenir un comportement spécifique

`Move.use` : Cette méthode est appelée à chaque fois qu'un personnage utilise le move. Elle est abstraite et doit être réimplémentée par les classes dérivées.

`Move.on_combat_begin` : Cette méthode est appelée au début d'un combat entre deux personnages. Elle est appelée une fois sur tous les moves des deux personnages impliqués dans le combat.

`Move.on_turn_begin` : Cette méthode est appelée au début de chaque tour d'un combat. Elle est appelée une fois sur tous les moves des deux personnages impliqués dans le combat, même si ce move n'a pas été utilisé. Elle est appelée avant que les personnages choisissent et effectuent leur action pour le tour.

Dans un combat entre les personnages A et B, l'ordre d'appel des méthodes auraient l'air de ceci :

`on_combat_begins` est appelé pour tous les moves de A et de B.

*Pour chaque tour* :

- `on_turn_begin` est appelé pour tous les moves de A et de B.

- Personnage **A** choisit et effectue son action (donc appelle de `use` sur l'action choisie)

- Personnage **B** choisit et effectue sont action (donc appelle de `use` sur l'action choisie)

## Action qui inflige du dommage (`character.SimpleDamagingMove`)

`SimpleDamagingMove` fait essentiellement la même chose que les armes dans le précédent exemple du chapitre 11. Sa méthode `use` calcule et applique le dommage selon la formule donnée par `utils.compute_std_damage_output` et retourne un message du genre :

```
Äpik took 54 dmg
```

On note qu'on a une méthode `compute_damage` qui fait le calcul de dommage seulement. On a une autre méthode `apply_damage` qui prend en paramètre le dommage à infliger et l'applique en retournant le message. Ces méthodes sont utilisée par `use` et peuvent surchargées.


## Actions magiques (*spells.py*)

C'est ici qu'on va créer des nouveaux types d'actions en étendant les actions de base. On ne fait aucun changement aux classes de base, on fait juste hériter de `Move` ou de `SimpleDamagingMove` en faisant les surcharges nécessaires pour 

### Absorber des HP (`DrainingMove`)

On veut créer une action qui cause du dommage à un adversaire et qui restaure une portion de ce dommage à l'attaquant. On a déjà une classe qui inflige du dommage directement, on va donc en hériter et ajuster l'exécution de sa méthode use.

On réalise que le calcul et l'application du dommage est déjà faite dans la classe de base (`compute_damage` et `apply_damage`) il faut juste ajouter une étape après (dans le `use`) qui calcule et applique les HP restorés et on l'ajoute au message déjà construit par l'étape précédente.

### Bonus incrémental (`IntensifyingMove`)

On veut un *move* qui gagne en puissance à mesure que le combat avance, donc à chaque tour. Ça rend cette action intéressante dans les combats qui durent plus longtemps.

On se rappelle qu'on peut surcharger `on_combat_begin` et `on_turn_begin` pour ajouter des comportements en dehors de l'utilisation directe. On remarque aussi qu'on veut faire la même chose que `SimpleDamagingMove` (même formule et même message), mais avec un bonus ajouter au dommage calculé. On peut surcharger `compute_damage` sans surcharger les autres.

## Déroulement du combat (`game.run_battle`)

C'est la fonction qui effectue un combat interactif en affichant les informations des deux personnages en demandant à l'usager d'entrer l'action à effectuer par chaque personnage.

Une exécution d'un tour du personnage *Gämmör* pourrait avoir l'aire de ceci :

```
Äpik                 lvl 70  | Gämmör               lvl 60
HP: 249/500                  | HP: 243/550
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
Select move for Gämmör:
    0: Unarmed Attack
    1: Slingshot
    2: Big Sucky

> 4
No can do, try something else
> f
No can do, try something else
> a
No can do, try something else
> 2

Gämmör used Big Sucky
  Critical hit! Äpik took 99 dmg
  Gämmör healed 50 HP

Enter a key to continue...
```



