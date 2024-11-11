"""
Chapitre 11.4

Code simulant le tri et l'exportation d'une playlist.
"""

import json
import os

from _music_library_version_prof import Playlist, Song


def manage_playlist(sort_key: str, file_path: str):
    """
    Crée une playlist, trie les chansons et exporte la liste triée au format JSON.

    :param sort_key: Clé selon laquelle trier les chansons (title, artist, duration, genre)
    :param file_path: Chemin pour exporter le fichier JSON
    """
    # Initialisation des chansons
    print("Initialisation des chansons...\n")
    songs = [
        Song("Blinding Lights", "The Weeknd", 200, "Pop"),
        Song("Shape of You", "Ed Sheeran", 240, "Pop"),
        Song("Bohemian Rhapsody", "Queen", 360, "Rock"),
        Song("Hotel California", "Eagles", 390, "Rock"),
        Song("Take Five", "Dave Brubeck", 324, "Jazz"),
    ]

    # Création de la playlist
    playlist = Playlist("My Favorites")
    for song in songs:
        playlist.add_song(song)

    # Affichage de la playlist initiale
    print("Playlist avant tri :\n")
    playlist.display()

    # Tri de la playlist
    print(f"\nTri des chansons par la clé nommée {sort_key}...\n")
    playlist.sort_songs(sort_key)
    playlist.display()

    # Exportation en JSON
    print(f"\nExportation de la playlist triée vers le fichier : {file_path} ...")
    playlist.export_to_json(file_path)
    print(f"Exportation réussie au chemin : {os.path.abspath(file_path)}")


def main():
    manage_playlist(sort_key="duration", file_path="sorted_playlist.json")

if __name__ == "__main__":
	main()