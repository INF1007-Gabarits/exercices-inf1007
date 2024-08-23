[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Notes et accords (chapitre 7)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indications contraires, vous devez retourner les résultats des fonctions, pas les afficher directement.

## Standard MIDI

Dans cette série d'exercices, nous utiliserons un clavier MIDI virtuel nous permettant de produire des notes musicales et la [librairie Mido](https://mido.readthedocs.io/en/latest/) en Python. Elle ne fait pas partie de la libraire standard de Python, il faut donc l'installer (soit avec `pip` ou à travers votre IDE). Pour nos besoin, disons seulement que le standard MIDI est un système de messages permettant de savoir quelles notes du clavier sont appuyées et relâchées. La librairie Mido nous permet d'obtenir ces messages dans un code Python et d'effectuer des actions sur ceux-ci.

## 1. Associations entre numéro MIDI et nom de notes
### `build_note_dictionaries`

Écrivez une fonction qui génère deux dictionnaires : un qui associe chaque numéro MIDI pertinent à un nom de note ("Do", "Ré", "C", "D", etc.) et un qui fait l'inverse. la fonction prend en paramètre le nom de chaque 12 notes de l'octave partant sur do. Le deuxième paramètre indique si les noms de notes doivent être suivis du numéro de l'octave (par exemple "C4" ou "C" pour le *middle C*).

Exemple :
```python
english_names = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
solfeggio_names = ["Do", "Réb", "Ré", "Mib", "Mi", "Fa", "Fa#", "Sol", "Lab", "La", "Sib", "Si"]
midi_to_name_eng_8va, name_to_midi_eng_8va = build_note_dictionaries(english_names, True)
midi_to_name_fr, name_to_midi_fr = build_note_dictionaries(solfeggio_names, False)
print(midi_to_name_eng_8va[64])
print(name_to_midi_eng_8va["C0"])
print(midi_to_name_fr[61])
print(midi_to_name_fr[73])
print(name_to_midi_fr["Fa#"])
```
Résultat :
```
E4
12
Réb
Réb
6
```

## 2. Afficher le nom des notes jouées
### `build_print_note_name_callback`

Écrivez une fonction qui retourne une fonction qui sert rappel (*callback*) et qui affiche le nom des notes qui sont jouées. On affiche seulement quand la note est appuyée, pas relâchée. On passe en paramètre à `build_print_note_name_callback` le dictionnaire d'associations de numéros MIDI à noms (le premier dictionnaire retourné par `build_note_dictionaries`).

Avec la librairie Mido, on peut assigner une fonction de rappel pour traiter les messages quand ils arrivent. Les callback de messages doivent être des fonctions (ou des objets fonctionnels) qui prennent en paramètre un message MIDI. On peut obtenir le type d'un message ([documentation](https://mido.readthedocs.io/en/latest/message_types.html)) via son `.type`. Si le type est `note_on`, on peut obtenir sa vitesse (le volume de la note) via son `.velocity`. On considère qu'une note est appuyées quand on a un message de type `note_on` avec une vitesse supérieure à 0. Une note est relâchée quand on a un `note_off` ou un `note_on` avec une vitesse de 0 (certains claviers envoient un `note_on` de volume 0 au lieu d'un `note_off`).

Voir exemple ci-dessous pour ouverture d'un port MIDI et enregistrement d'un callback.

Exemple :
```python
midi_to_name, name_to_midi = build_note_dictionaries(solfeggio_names, True)
print_note_name = build_print_note_name_callback(midi_to_name)
keyboard = mido.open_input("UnPortMIDI 0", callback=print_note_name)
# Maintenant les notes vont s'afficher

input("Affichage des noms de notes (Appuyez sur ENTER pour passer à l'étape suivante)..." "\n")
```
Résultat si on fait une gamme de do majeur dans l'octave 4 :
```
Affichage des noms de notes (Appuyez sur ENTER pour passer à l'étape suivante)...
Do4
Ré4
Mi4
Fa4
Sol4
La4
Si4
Do5
```

## 3. Afficher les noms d'accords
### `build_print_chord_name_callback`

Écrivez une fonction qui retourne une fonction qui sert callback et qui affiche le nom des accords qui sont joués. On affiche seulement quand seulement les notes de l'accord sont appuyées, pas relâchées, et on ne s'occupe pas des arpèges. On passe en paramètre à `build_print_chord_name_callback` un dictionnaire d'associations notes et de nom d'accords suivi d'un dictionnaire de noms à numéro MIDI (le deuxième dictionnaire retourné par `build_note_dictionaries`).

Exemple :
```python
chord_names = {
    "Do majeur" : ("Do", "Mi", "Sol"),
    "Fa majeur" : ("Fa", "La", "Do"),
    "Sol majeur" : ("Sol", "Si", "Ré"),
}
midi_to_name, name_to_midi = build_note_dictionaries(solfeggio_names, False)
print_chord_name = build_print_chord_name_callback(chord_names, name_to_midi)
keyboard = mido.open_input("UnPortMIDI 0", callback=print_chord_name)

input("Affichage des noms d'accords (Appuyez sur ENTER pour passer à l'étape suivante)..." "\n")
```
Résultat si on joue IV-V-I en do majeur :
```
Affichage des noms d'accords (Appuyez sur ENTER pour passer à l'étape suivante)...
Fa majeur
Sol majeur
Do majeur
```
