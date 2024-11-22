import pygame
import random
import time
import math

# Initialiser Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 700, 800  # Taille de la fenêtre de jeu
TILE_SIZE = 40  # Taille des cases pour des proportions cohérentes
GRID_ROWS = 9  # Nombre de rangées, peut aussi être 16
GRID_COLS = 9  # Nombre de colonnes, peut aussi être 16
BOMB_COUNT = 15  # Nombre standard de bombes pour le démineur, peut aussi être 40
HEADER_HEIGHT = 100  # Hauteur de l'en-tête pour la zone supérieure

# Calculer dynamiquement la largeur de la grille et de l'en-tête
GRID_WIDTH = WIDTH - 50  # Légèrement plus petit que la largeur totale de la fenêtre
HEADER_WIDTH = GRID_WIDTH  # Faire correspondre la largeur de la grille à celle de l'en-tête

# Ajuster dynamiquement la taille des cases pour s'adapter à la largeur de la grille
TILE_SIZE = GRID_WIDTH // GRID_COLS

# Calculer la hauteur de la grille en fonction du nombre de rangées
GRID_HEIGHT = TILE_SIZE * GRID_ROWS

# Calculer les décalages pour centrer la grille
OFFSET_X = (WIDTH - GRID_WIDTH) // 2  # Centrer horizontalement la grille et l'en-tête
OFFSET_Y = HEADER_HEIGHT + 20  # Positionner la grille légèrement en dessous de l'en-tête

# Variables globales pour l'état du jeu
game_over = False  # Initialiser la variable game_over
start_time = None  # Initialiser la variable start_time
elapsed_time = 0  # Variable pour enregistrer le temps écoulé

# Couleurs
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

NUMBER_COLORS = {
    1: BLUE,
    2: GREEN,
    3: RED,
    4: (0, 0, 139),  # Bleu foncé
    5: (139, 0, 0),  # Rouge foncé
    6: (0, 139, 139),  # Cyan
    7: BLACK,
    8: GRAY,
}

# Configuration de l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Démineur")

# Police
font = pygame.font.SysFont(None, 60)

# Fonction pour dessiner l'en-tête
def draw_header(remaining_bombs, elapsed_time, game_over, player_won):
    # Définir la largeur de l'en-tête (identique à la grille)
    header_width = GRID_COLS * TILE_SIZE
    header_x = (WIDTH - header_width) // 2 - 3  # Centrer l'en-tête horizontalement
    header_rect = pygame.Rect(header_x, 0, header_width, HEADER_HEIGHT)

    # Dessiner le remplissage gris de base pour l'en-tête
    pygame.draw.rect(screen, GRAY, header_rect)

    # Ajouter un effet 3D : bord clair en haut à gauche et bord foncé en bas à droite
    pygame.draw.line(screen, DARK_GRAY, header_rect.topleft, header_rect.topright, 3)  # Bord supérieur
    pygame.draw.line(screen, DARK_GRAY, header_rect.topleft, header_rect.bottomleft, 3)  # Bord gauche
    pygame.draw.line(screen, WHITE, header_rect.bottomleft, header_rect.bottomright, 3)  # Bord inférieur
    pygame.draw.line(screen, WHITE, header_rect.topright, header_rect.bottomright, 3)  # Bord droit

    # Dessiner le nombre de bombes restantes
    bomb_count_text = font.render(f"{remaining_bombs:03}", True, RED)
    bomb_count_rect = bomb_count_text.get_rect(center=(WIDTH // 8, HEADER_HEIGHT // 2))
    screen.blit(bomb_count_text, bomb_count_rect)

    # Visage souriant dans une boîte 3D
    smiley_box_size = HEADER_HEIGHT // 1.5
    smiley_box_x = header_x + header_width // 2 - smiley_box_size // 2
    smiley_box_y = HEADER_HEIGHT // 2 - smiley_box_size // 2
    smiley_box_rect = pygame.Rect(smiley_box_x, smiley_box_y, smiley_box_size, smiley_box_size)

    # Dessiner la boîte 3D
    pygame.draw.rect(screen, GRAY, smiley_box_rect)  # Fond de la boîte
    pygame.draw.line(screen, WHITE, smiley_box_rect.topleft, smiley_box_rect.topright, 3)  # Bord supérieur
    pygame.draw.line(screen, WHITE, smiley_box_rect.topleft, smiley_box_rect.bottomleft, 3)  # Bord gauche
    pygame.draw.line(screen, DARK_GRAY, smiley_box_rect.bottomleft, smiley_box_rect.bottomright, 3)  # Bord inférieur
    pygame.draw.line(screen, DARK_GRAY, smiley_box_rect.topright, smiley_box_rect.bottomright, 3)  # Bord droit

    # Dessiner le visage souriant
    smiley_center_x = smiley_box_x + smiley_box_size // 2
    smiley_center_y = smiley_box_y + smiley_box_size // 2
    smiley_radius = smiley_box_size // 3
    pygame.draw.circle(screen, YELLOW, (smiley_center_x, smiley_center_y), smiley_radius)
    pygame.draw.circle(screen, BLACK, (smiley_center_x, smiley_center_y), smiley_radius, 2)

    if player_won:
        # Visage souriant avec des lunettes de soleil
        pygame.draw.rect(screen, BLACK, (smiley_center_x - 15, smiley_center_y - 15, 12, 6))  # Lentille gauche
        pygame.draw.rect(screen, BLACK, (smiley_center_x + 3, smiley_center_y - 15, 12, 6))  # Lentille droite
        pygame.draw.line(screen, BLACK, (smiley_center_x - 3, smiley_center_y - 12), (smiley_center_x + 3, smiley_center_y - 12), 2)  # Pont
        pygame.draw.arc(screen, BLACK, (smiley_center_x - 10, smiley_center_y + 5, 20, 10), 3.14, 0, 2)  # Sourire
    elif game_over:
        # Visage mort
        pygame.draw.line(screen, BLACK, (smiley_center_x - 10, smiley_center_y - 10), (smiley_center_x - 5, smiley_center_y - 5), 2)
        pygame.draw.line(screen, BLACK, (smiley_center_x - 10, smiley_center_y - 5), (smiley_center_x - 5, smiley_center_y - 10), 2)
        pygame.draw.line(screen, BLACK, (smiley_center_x + 5, smiley_center_y - 10), (smiley_center_x + 10, smiley_center_y - 5), 2)
        pygame.draw.line(screen, BLACK, (smiley_center_x + 5, smiley_center_y - 5), (smiley_center_x + 10, smiley_center_y - 10), 2)
        pygame.draw.arc(screen, BLACK, (smiley_center_x - 10, smiley_center_y, 20, 10), 0, 3.14, 2)  # Bouche triste
    else:
        # Visage souriant normal
        pygame.draw.circle(screen, BLACK, (smiley_center_x - 7, smiley_center_y - 7), 3)  # Oeil gauche
        pygame.draw.circle(screen, BLACK, (smiley_center_x + 7, smiley_center_y - 7), 3)  # Oeil droit
        pygame.draw.arc(screen, BLACK, (smiley_center_x - 10, smiley_center_y + 5, 20, 10), 3.14, 0, 2)  # Sourire

    # Dessiner le chronomètre
    timer_text = font.render(f"{elapsed_time:03}", True, RED)
    timer_rect = timer_text.get_rect(center=(7 * WIDTH // 8, HEADER_HEIGHT // 2))
    screen.blit(timer_text, timer_rect)


# Classe pour la case de base
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_revealed = False
        self.is_flagged = False

    def draw(self):
        rect = pygame.Rect(self.x * TILE_SIZE + OFFSET_X, self.y * TILE_SIZE + OFFSET_Y, TILE_SIZE, TILE_SIZE)

        if not self.is_revealed:  # Case non révélée (en relief)
            # Remplissage gris de base
            pygame.draw.rect(screen, GRAY, rect)

            # Ajouter un effet 3D en relief
            pygame.draw.line(screen, WHITE, rect.topleft, rect.topright, 2)  # Bord supérieur
            pygame.draw.line(screen, WHITE, rect.topleft, rect.bottomleft, 2)  # Bord gauche
            pygame.draw.line(screen, DARK_GRAY, rect.bottomleft, rect.bottomright, 2)  # Bord inférieur
            pygame.draw.line(screen, DARK_GRAY, rect.topright, rect.bottomright, 2)  # Bord droit
        elif self.is_revealed:  # Case révélée (enfoncée)
            # Remplissage gris clair de base
            pygame.draw.rect(screen, GRAY, rect)

            # Ajouter un effet 3D enfoncé
            pygame.draw.line(screen, DARK_GRAY, rect.topleft, rect.topright, 2)  # Bord supérieur
            pygame.draw.line(screen, DARK_GRAY, rect.topleft, rect.bottomleft, 2)  # Bord gauche
            pygame.draw.line(screen, WHITE, rect.bottomleft, rect.bottomright, 2)  # Bord inférieur
            pygame.draw.line(screen, WHITE, rect.topright, rect.bottomright, 2)  # Bord droit

        # Dessiner le drapeau si la case est marquée
        if self.is_flagged and not self.is_revealed:
            # Base du drapeau (rectangle noir)
            base_x = self.x * TILE_SIZE + OFFSET_X + TILE_SIZE // 4
            base_y = self.y * TILE_SIZE + OFFSET_Y + TILE_SIZE // 2 + TILE_SIZE // 4
            pygame.draw.rect(screen, BLACK, (base_x, base_y, TILE_SIZE // 2, TILE_SIZE // 6))

            # Mât du drapeau (ligne verticale noire)
            pole_x = self.x * TILE_SIZE + OFFSET_X + TILE_SIZE // 2
            pole_y_start = self.y * TILE_SIZE + OFFSET_Y + TILE_SIZE // 4
            pole_y_end = self.y * TILE_SIZE + OFFSET_Y + TILE_SIZE // 2 + TILE_SIZE // 4
            pygame.draw.line(screen, BLACK, (pole_x, pole_y_start), (pole_x, pole_y_end), 2)

            # Pointe du drapeau (triangle rouge)
            triangle_points = [
                (pole_x, pole_y_start),  # Sommet du triangle
                (pole_x + TILE_SIZE // 4, pole_y_start + TILE_SIZE // 8),  # Coin inférieur droit
                (pole_x, pole_y_start + TILE_SIZE // 8),  # Coin inférieur gauche
            ]
            pygame.draw.polygon(screen, RED, triangle_points)


class BombTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_triggered = False  # Indique si cette bombe a été déclenchée

    def draw(self):
        # Utiliser la méthode de la classe parente pour l'état non révélé
        if not self.is_revealed and not self.is_triggered:
            super().draw()  # Dessiner la case comme une case normale non révélée
        else:
            rect = pygame.Rect(self.x * TILE_SIZE + OFFSET_X, self.y * TILE_SIZE + OFFSET_Y, TILE_SIZE, TILE_SIZE)

            # Changer la couleur de fond en fonction de l'état
            if self.is_triggered:  # Si cette bombe est déclenchée, le fond devient rouge
                pygame.draw.rect(screen, RED, rect)
            elif self.is_revealed:  # Si révélée mais pas déclenchée, utiliser la couleur normale
                pygame.draw.rect(screen, DARK_GRAY, rect)

            # Dessiner le bord
            pygame.draw.rect(screen, BLACK, rect, 2)

            # Dessiner la bombe
            center_x = self.x * TILE_SIZE + TILE_SIZE // 2 + OFFSET_X
            center_y = self.y * TILE_SIZE + TILE_SIZE // 2 + OFFSET_Y
            radius = TILE_SIZE // 4

            # Dessiner le noyau noir de la bombe
            pygame.draw.circle(screen, BLACK, (center_x, center_y), radius)

            # Dessiner les lignes autour du noyau
            line_length = radius + 6  # Longueur des lignes à partir du centre
            num_lines = 8  # Nombre de lignes

            for i in range(num_lines):
                # Calculer l'angle de chaque ligne
                angle = 2 * math.pi * i / num_lines

                # Définir le point de départ (bord du cercle noir)
                start_x = center_x + int(radius * math.cos(angle))
                start_y = center_y + int(radius * math.sin(angle))

                # Définir le point d'arrivée (extrémité de la ligne)
                end_x = center_x + int(line_length * math.cos(angle))
                end_y = center_y + int(line_length * math.sin(angle))

                # Dessiner la ligne
                pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 3)

            # Dessiner la lueur centrale (petit cercle blanc)
            pygame.draw.circle(screen, WHITE, (center_x - 4, center_y - 5), radius // 4)


class NumberTile(Tile):
    def __init__(self, x, y, number):
        super().__init__(x, y)
        self.number = number

    def draw(self):
        super().draw()
        if self.is_revealed and self.number > 0:
            # Dessiner le numéro au centre de la case
            text = font.render(str(self.number), True, NUMBER_COLORS[self.number])
            text_rect = text.get_rect(center=(
                self.x * TILE_SIZE + TILE_SIZE // 2 + OFFSET_X,
                self.y * TILE_SIZE + TILE_SIZE // 2 + OFFSET_Y,
            ))
            screen.blit(text, text_rect)


# Plateau de jeu
class Board:
    def __init__(self, rows, cols, bomb_count):
        self.rows = rows
        self.cols = cols
        self.bomb_count = bomb_count
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.remaining_flags = bomb_count
        self.create_board()

    def create_board(self):
        # Générer les positions des bombes
        bomb_positions = set()
        while len(bomb_positions) < self.bomb_count:
            bomb_positions.add(
                (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            )

        # Remplir la grille avec des bombes ou des cases numériques
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in bomb_positions:
                    self.grid[row][col] = BombTile(col, row)
                else:
                    number = self.count_adjacent_bombs(row, col, bomb_positions)
                    self.grid[row][col] = NumberTile(col, row, number)

    def count_adjacent_bombs(self, row, col, bomb_positions):
        # Compter le nombre de bombes adjacentes à une case donnée
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if 0 <= row + dr < self.rows and 0 <= col + dc < self.cols:
                    if (row + dr, col + dc) in bomb_positions:
                        count += 1
        return count

    def reveal_tile(self, x, y):
        global game_over, elapsed_time
        tile = self.grid[y][x]
        if not tile.is_revealed and not tile.is_flagged:
            tile.is_revealed = True
            if isinstance(tile, BombTile):
                game_over = True
                tile.is_triggered = True  # Marquer cette bombe comme déclenchée
                # Geler le chronomètre lorsque le jeu est terminé
                elapsed_time = int(time.time() - start_time)
            elif isinstance(tile, NumberTile) and tile.number == 0:
                self.reveal_adjacent_tiles(x, y)

    def toggle_flag(self, x, y):
        # Basculer l'état de drapeau sur une case
        tile = self.grid[y][x]
        if not tile.is_revealed:
            tile.is_flagged = not tile.is_flagged
            self.remaining_flags += -1 if tile.is_flagged else 1

    def reveal_adjacent_tiles(self, x, y):
        # Révéler les cases adjacentes à une case vide
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.cols and 0 <= ny < self.rows:
                    self.reveal_tile(nx, ny)

    def draw(self):
        # Dessiner toutes les cases du plateau
        for row in self.grid:
            for tile in row:
                tile.draw()

    def check_win_condition(self):
        # Vérifier si le joueur a gagné
        for row in self.grid:
            for tile in row:
                if isinstance(tile, BombTile) and not tile.is_flagged:
                    return False  # Toutes les bombes doivent être marquées
                if isinstance(tile, NumberTile) and not tile.is_revealed:
                    return False  # Toutes les cases numériques doivent être révélées
        return True  # Si toutes les conditions sont satisfaites, le joueur a gagné

# Jeu principal
def main():
    global game_over, start_time, elapsed_time
    clock = pygame.time.Clock()  # Création d'un objet horloge pour gérer les FPS du jeu
    running = True  # Variable pour maintenir la boucle principale en cours d'exécution
    board = Board(GRID_ROWS, GRID_COLS, BOMB_COUNT)  # Initialiser le plateau de jeu avec des tuiles et des bombes
    start_time = time.time()  # Enregistrer le temps de début de la partie
    player_won = False  # Variable pour suivre si le joueur a gagné

    while running:  # Boucle principale du jeu
        screen.fill(GRAY)  # Remplir l'écran avec une couleur de fond

        # Mettre à jour le chronomètre si le jeu est en cours
        if not game_over and not player_won:
            elapsed_time = int(time.time() - start_time)  # Calculer le temps écoulé

        # Dessiner l'en-tête (compteur de bombes, chronomètre, visage souriant)
        draw_header(board.remaining_flags, elapsed_time, game_over, player_won)

        # Dessiner le plateau de jeu (grille de tuiles)
        board.draw()

        # Gérer les événements (clics de souris, fermeture de la fenêtre, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
                running = False  # Arrêter la boucle principale

            if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic de souris est détecté
                x, y = event.pos  # Obtenir les coordonnées du clic

                # Vérifier si le visage souriant est cliqué (pour redémarrer le jeu)
                smiley_center_x = WIDTH // 2  # Centre horizontal du visage souriant
                smiley_center_y = HEADER_HEIGHT // 2  # Centre vertical du visage souriant
                smiley_radius = HEADER_HEIGHT // 3  # Rayon du visage souriant
                distance_from_smiley = ((x - smiley_center_x) ** 2 + (y - smiley_center_y) ** 2) ** 0.5  # Distance entre le clic et le centre du visage

                if distance_from_smiley <= smiley_radius:  # Si le clic est à l'intérieur du visage
                    # Réinitialiser le jeu : recréer le plateau et réinitialiser les variables
                    board = Board(GRID_ROWS, GRID_COLS, BOMB_COUNT)
                    game_over = False
                    player_won = False
                    start_time = time.time()  # Réinitialiser le temps de départ
                    elapsed_time = 0  # Réinitialiser le chronomètre

                # Si le clic est sur le plateau de jeu et le jeu est en cours
                elif not game_over and not player_won and y > HEADER_HEIGHT:
                    # Convertir les coordonnées du clic en indices de la grille
                    x = (x - OFFSET_X) // TILE_SIZE
                    y = (y - OFFSET_Y) // TILE_SIZE

                    # Vérifier si les indices sont valides (dans les limites de la grille)
                    if 0 <= x < GRID_COLS and 0 <= y < GRID_ROWS:
                        if event.button == 1:  # Si clic gauche
                            board.reveal_tile(x, y)  # Révéler la tuile cliquée
                        elif event.button == 3:  # Si clic droit
                            board.toggle_flag(x, y)  # Basculer un drapeau sur la tuile

                # Vérifier si toutes les conditions de victoire sont remplies après l'action
                if not game_over and board.check_win_condition():
                    player_won = True  # Marquer que le joueur a gagné

        # Rafraîchir l'écran après chaque itération de la boucle
        pygame.display.flip()
        clock.tick(60)  # Fixer la fréquence d'images à 60 FPS


if __name__ == "__main__":
    main()
