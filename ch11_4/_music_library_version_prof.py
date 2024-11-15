"""
Chapitre 11.4

Classes pour représenter une bibliothèque musicale.
"""

class Song:
    """
    Une chanson dans la bibliothèque.

    :param title:       Le titre de la chanson
    :param artist:      L'artiste de la chanson
    :param duration:    La durée de la chanson en secondes
    :param genre:       Le genre musical
    """

    def __init__(self, title, artist, duration, genre):
        self.__title = title
        self.__artist = artist
        self.duration = duration
        self.genre = genre

    @property
    def title(self):
        return self.__title

    @property
    def artist(self):
        return self.__artist

    def __str__(self):
        mins, secs = divmod(self.duration, 60)
        return f"{self.title} by {self.artist} - {mins}:{secs:02} ({self.genre})"

    def to_dict(self):
        """
        Convertit une chanson en dictionnaire.
        """
        return {
            "title": self.title,
            "artist": self.artist,
            "duration": self.duration,
            "genre": self.genre,
        }



class Playlist:
    """
    Une playlist contenant plusieurs chansons.

    :param name:  Le nom de la playlist
    """

    def __init__(self, name):
        self.__name = name
        self.songs = []

    @property
    def name(self):
        return self.__name

    def add_song(self, song):
        """
        Ajoute une chanson à la playlist.
        """
        if not isinstance(song, Song):
            raise TypeError("Only Song objects can be added to the playlist.")
        self.songs.append(song)

    def sort_songs(self, key):
        """
        Trie les chansons selon la clé.
        """
        valid_keys = {"title", "artist", "duration", "genre"}
        if key not in valid_keys:
            raise ValueError(f"Invalid sort key. Choose from {valid_keys}.")
        self.songs.sort(key=lambda song: getattr(song, key))

    def total_duration(self):
        """
        Calcule la durée totale de la playlist.
        """
        return sum(song.duration for song in self.songs)

    def display(self):
        """
        Affiche la liste des chansons dans la playlist.
        """
        print(f"Playlist: {self.name}")
        for index, song in enumerate(self.songs, 1):
            print(f"{index}. {song}")
        mins, secs = divmod(self.total_duration(), 60)
        print(f"Total duration: {mins} min {secs} sec")
    
    def export_to_json(self, file_path):
        """
        Exporte la playlist triée au format JSON dans un fichier.
        
        :param file_path: Chemin pour sauvegarder le fichier JSON.
        """
        playlist_dict = [song.to_dict() for song in self.songs]
        with open(file_path, "w", encoding="utf-8") as file:
            import json
            json.dump(playlist_dict, file, ensure_ascii=False, indent=4)
        print(f"Playlist exportée avec succès dans : {file_path}")
    
    
    
