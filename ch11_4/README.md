
# Bibliothèque musicale (Chapitre 11)

Nous allons programmer une classe représentant une chanson et une autre pour gérer une liste de lecture musicale. Cela permettra de manipuler des objets comme des chansons et d'effectuer des opérations telles qu'ajouter une chanson, trier une playlist et exporter la liste triée au format JSON. Le tri et l'exportation sont gérés via la fonction `manage_playlist` dans le fichier `exercice.py`.

---

## Chansons (`music_library.Song`)

On veut une classe qui représente une chanson. Une chanson possède les attributs suivants :
- **`title`** : Le titre de la chanson (ne peut pas être modifié après initialisation).
- **`artist`** : L'artiste ayant produit la chanson (ne peut pas être modifié après initialisation).
- **`duration`** : La durée de la chanson en secondes.
- **`genre`** : Le genre musical (par exemple, Pop, Rock, Jazz).

La classe inclut également une méthode spéciale `__str__` qui retourne une description lisible de la chanson au format suivant :  
`"{titre} by {artiste} - {minutes}:{secondes} ({genre})"`

### Exemple d'utilisation :

```python
song = Song("Blinding Lights", "The Weeknd", 200, "Pop")
print(song)
```

Sortie :
```vbnet
Blinding Lights by The Weeknd - 3:20 (Pop)
```

---

## Listes de lecture (`music_library.Playlist`)

On veut une classe qui représente une liste de lecture musicale. Une playlist possède les attributs suivants :
- **`name`** : Le nom de la playlist (ne peut pas être modifié après initialisation).
- **`songs`** : Une liste contenant des objets `Song`.

La playlist inclut plusieurs méthodes pour gérer les chansons et calculer des informations.

### Méthodes :

#### `add_song(song)`
Ajoute une chanson à la playlist. Si l'objet passé n'est pas une instance de `Song`, une erreur de type `TypeError` est levée.

#### `sort_songs(key)`
Trie les chansons de la playlist selon une clé donnée. Les clés valides sont :
- `"title"` : Trie par titre.
- `"artist"` : Trie par artiste.
- `"duration"` : Trie par durée.
- `"genre"` : Trie par genre.

#### `total_duration()`
Calcule et retourne la durée totale de toutes les chansons de la playlist (en secondes).

#### `display()`
Affiche toutes les chansons contenues dans la playlist, ainsi que la durée totale formatée (en minutes et secondes).

### Exemple d'utilisation :

```python
# Création des chansons
song1 = Song("Blinding Lights", "The Weeknd", 200, "Pop")
song2 = Song("Shape of You", "Ed Sheeran", 240, "Pop")
song3 = Song("Bohemian Rhapsody", "Queen", 360, "Rock")

# Création de la playlist
playlist = Playlist("My Favorites")
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)

# Affichage de la playlist
playlist.display()
```

Sortie :
```vbnet
Playlist: My Favorites
1. Blinding Lights by The Weeknd - 3:20 (Pop)
2. Shape of You by Ed Sheeran - 4:00 (Pop)
3. Bohemian Rhapsody by Queen - 6:00 (Rock)
Total duration: 13 min 20 sec
```

---

## Fonctionnalités de gestion (`exercice.py`)

Le fichier `exercice.py` implémente une fonction `manage_playlist` qui simule la gestion de playlists en Python. Cette fonction effectue les actions suivantes :
1. Crée une playlist contenant plusieurs chansons.
2. Affiche la playlist initiale.
3. Trie les chansons selon une clé donnée.
4. Affiche la playlist triée.
5. Exporte la playlist triée dans un fichier JSON dans un nouveau dossier nommé `libraries`.

### Exemple d'utilisation de `manage_playlist` :

```python
from music_library import Playlist, Song

def manage_playlist(sort_key: str, file_path: str):
    songs = [
        Song("Blinding Lights", "The Weeknd", 200, "Pop"),
        Song("Shape of You", "Ed Sheeran", 240, "Pop"),
        Song("Bohemian Rhapsody", "Queen", 360, "Rock"),
        Song("Hotel California", "Eagles", 390, "Rock"),
        Song("Take Five", "Dave Brubeck", 324, "Jazz"),
    ]

    playlist = Playlist("My Favorites")
    for song in songs:
        playlist.add_song(song)

    print("Playlist avant tri :")
    playlist.display()

    playlist.sort_songs(sort_key)
    print(f"Playlist triée par {sort_key} :")
    playlist.display()

    playlist.export_to_json(file_path)
    print(f"Playlist exportée dans le fichier : {file_path}")
```

---

### Exemple d'exécution :

Appeler la fonction dans un script ou depuis un terminal :

```python
if __name__ == "__main__":
    manage_playlist(sort_key="duration", file_path="sorted_playlist.json")
```

Sortie console :
```vbnet
Initialisation des chansons...

Playlist avant tri :

Playlist: My Favorites
1. Blinding Lights by The Weeknd - 3:20 (Pop)
2. Shape of You by Ed Sheeran - 4:00 (Pop)
3. Bohemian Rhapsody by Queen - 6:00 (Rock)
4. Hotel California by Eagles - 6:30 (Rock)
5. Take Five by Dave Brubeck - 5:24 (Jazz)
Total duration: 25 min 14 sec

Tri des chansons par la clé nommée duration...

Playlist: My Favorites
1. Blinding Lights by The Weeknd - 3:20 (Pop)
2. Shape of You by Ed Sheeran - 4:00 (Pop)
3. Take Five by Dave Brubeck - 5:24 (Jazz)
4. Bohemian Rhapsody by Queen - 6:00 (Rock)
5. Hotel California by Eagles - 6:30 (Rock)
Total duration: 25 min 14 sec
Répertoire 'libraries' créé.

Exportation de la playlist triée vers le fichier : libraries\sorted_playlist.json ...
Playlist exportée avec succès dans : libraries\sorted_playlist.json
Exportation réussie au chemin : (votre chemin absolu)\sorted_playlist.json
```

---
