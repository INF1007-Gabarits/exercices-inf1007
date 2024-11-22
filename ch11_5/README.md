# Jeu du démineur (minesweeper)! (Chapitre 11)

Dans ce projet, nous allons construire un jeu de Démineur en utilisant une approche orientée objet. L'objectif est de créer un plateau de jeu interactif où les joueurs doivent éviter les bombes tout en dévoilant les cases sûres.

Le jeu du Démineur suit ces règles :
- Le joueur clique sur des cases pour les révéler.
- Une case révélée affiche soit un chiffre (indiquant le nombre de bombes dans les cases adjacentes), soit une bombe (ce qui termine la partie).
- Le joueur peut marquer une case suspectée de contenir une bombe avec un drapeau.
- **La partie est gagnée lorsque toutes les cases sans bombes sont révélées et toutes les bombes correctement marquées.**

Nous utiliserons la bibliothèque **Pygame** pour gérer l'interface graphique et les interactions utilisateur. Installez-la si nécessaire avec la commande :
```bash
pip install pygame
```

Avec le code de départ fourni dans `minesweeper.py`, nous allons étendre les fonctionnalités pour aboutir à un jeu complet.

---

## **Étape 1 : Comprendre et étendre `Tile`**

La classe `Tile` est la base de toutes les cases du plateau. Elle gère :
- **Position** : `x, y` sur la grille.
- **État** : Révélée (`is_revealed`) ou marquée avec un drapeau (`is_flagged`).
- **Affichage** : La méthode `draw()` rend la case à l'écran en fonction de son état.

Voici ce que vous devez faire pour enrichir cette classe :
1. **Créer des sous-classes pour les types spécifiques de cases :**
   - **`BombTile`** :
     - Représente une case contenant une bombe.
     - Ajoutez un attribut `is_triggered` pour signaler si la bombe a été déclenchée.
     - Surchargez `draw()` pour afficher une bombe lorsqu'elle est révélée.
   - **`NumberTile`** :
     - Représente une case qui affiche le nombre de bombes adjacentes.
     - Ajoutez un attribut `number` pour stocker ce nombre.
     - Surchargez `draw()` pour afficher le chiffre.

### Exemple :
```python
class BombTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_triggered = False

    def draw(self):
        # Utiliser super() pour les états non révélés
        if not self.is_revealed:
            super().draw()
        else:
            # Code pour afficher une bombe (ex. un cercle rouge ou noir)
```

---

## **Étape 2 : Créer et gérer le plateau avec `Board`**

La classe `Board` représente le plateau entier. Elle est responsable de :
- **Initialisation** :
  - Générer des bombes aléatoires.
  - Calculer le nombre de bombes adjacentes pour les cases sûres.
- **Gestion des interactions** :
  - Révéler une case (`reveal_tile`).
  - Marquer une case (`toggle_flag`).
  - Gérer les révélations en cascade pour les cases vides.
- **Détection de la victoire** :
  - Vérifier si toutes les cases sûres sont révélées et toutes les bombes correctement marquées.

### Tâches à réaliser :
1. **Créer une méthode `create_board`** :
   - Placez des bombes aléatoirement.
   - Remplissez les cases restantes avec des `NumberTile`.
   - Calculez les bombes adjacentes pour chaque `NumberTile`.

2. **Implémentez les interactions utilisateur** :
   - `reveal_tile(x, y)` : Révèle une case et gère les cascades si elle est vide.
   - `toggle_flag(x, y)` : Marque ou démarque une case avec un drapeau.

3. **Ajoutez la détection de la victoire** :
   - Implémentez une méthode `check_win_condition` pour vérifier si toutes les bombes sont marquées et toutes les cases sûres révélées.
   - Retournez `True` si le joueur a gagné, sinon `False`.

4. **Ajoutez l'affichage** :
   - La méthode `draw()` affiche toutes les cases du plateau.

---

## **Étape 3 : Gérer l'interface avec `draw_header`**

La fonction `draw_header` est déjà fournie et permet d'afficher :
- Le nombre de bombes restantes.
- Le chronomètre.
- Le visage souriant, qui permet de redémarrer la partie.

Voici comment elle s'intègre dans la boucle principale du jeu :
- Elle est appelée à chaque itération pour afficher l'état actuel.
- Le visage souriant peut être cliqué pour réinitialiser le jeu.
- Modifiez-la pour afficher un visage de victoire si `check_win_condition` retourne `True`.

### Exemple :
```python
if player_won:
    # Dessiner un visage souriant avec des lunettes
    pygame.draw.rect(screen, BLACK, (smiley_center_x - 15, smiley_center_y - 15, 12, 6))  # Lunettes gauche
    pygame.draw.rect(screen, BLACK, (smiley_center_x + 3, smiley_center_y - 15, 12, 6))  # Lunettes droite
```

---

## **Étape 4 : La boucle principale**

La boucle principale du jeu  dans la fonction `main` gère :
1. **Initialisation** :
   - Créez un objet `Board` pour le plateau.
   - Initialisez les variables globales comme `game_over`, `player_won` et `elapsed_time`.

2. **Gestion des événements** :
   - Gérer les clics gauche pour révéler une case.
   - Gérer les clics droits pour marquer une case.
   - Vérifier si le visage souriant est cliqué pour redémarrer.

3. **Vérification de la victoire** :
   - Appelez `check_win_condition` après chaque interaction pour voir si le joueur a gagné.

4. **Affichage** :
   - Appelez `draw_header` et `board.draw()` pour actualiser l'écran.

---

## Résumé

- **Étape 1 :** Implémentez `BombTile` et `NumberTile` pour enrichir `Tile`.
- **Étape 2 :** Développez `Board` pour gérer les interactions et détecter la victoire avec `check_win_condition`.
- **Étape 3 :** Intégrez `draw_header` pour afficher les informations du jeu et le visage souriant.
- **Étape 4 :** Créez une boucle principale pour gérer les événements, afficher le plateau, et détecter la victoire.

Une fois ces étapes complétées, vous aurez un jeu de Démineur entièrement fonctionnel !
