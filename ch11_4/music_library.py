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

    # TODO: __init__
    # Ajouter un constructeur qui initialise le titre, l'artiste, la durée et le genre d'une chanson.

    # TODO: Propriétés
    # Ajouter les propriétés en lecture seule pour `title` et `artist`.

    # TODO: __str__
    # Implémenter la méthode spéciale pour afficher une chanson au format :
    # "{title} by {artist} - {minutes}:{seconds} ({genre})"

    # TODO: to_dict
    # Ajouter une méthode qui convertit les attributs de la chanson en dictionnaire.

    pass


class Playlist:
    """
    Une playlist contenant plusieurs chansons.

    :param name:  Le nom de la playlist
    """

    # TODO: __init__
    # Ajouter un constructeur qui initialise le nom de la playlist et une liste vide pour les chansons.

    # TODO: Propriété pour `name`
    # Ajouter une propriété en lecture seule pour le nom de la playlist.

    # TODO: add_song
    # Ajouter une méthode qui ajoute une chanson à la liste des chansons.
    # Si l'objet ajouté n'est pas une instance de `Song`, lever une erreur `TypeError`.

    # TODO: sort_songs
    # Ajouter une méthode qui trie les chansons selon une clé donnée (`title`, `artist`, `duration`, ou `genre`).
    # Lever une erreur si la clé n'est pas valide.

    # TODO: total_duration
    # Ajouter une méthode qui calcule et retourne la durée totale de toutes les chansons de la playlist.

    # TODO: display
    # Ajouter une méthode qui affiche les chansons dans la playlist avec leur durée totale.

    # TODO: export_to_json
    # Ajouter une méthode qui exporte la playlist triée au format JSON dans un fichier.

    pass
