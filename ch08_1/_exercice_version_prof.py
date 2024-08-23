#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
import pickle
import json

from recettes import add_recipes, delete_recipe, print_recipe, run_interactive


def exercice1(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, encoding="utf-8") as f2:
        for count, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"The files are not identical. Line {count + 1} is different.")
                print(line1)
                print("Is not the same as:")
                print(line2)

                return

    print("The files are identical")

def exercice2(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        f2.write(f1.read().replace(" ", "   "))

def exercice3(note_path, thresholds_file_path, result_file_path):
    with open(note_path, encoding="utf-8") as note_file:
        notes_percent = note_file.readlines()  # To get rid of \n: note_file.read().splitlines()

    with open(thresholds_file_path, "r") as thresholds_file:
        letter_grade_thresholds = json.load(thresholds_file)

    with open(result_file_path, "w", encoding="utf-8") as result_file:
        for note in notes_percent:
            for key, value in letter_grade_thresholds.items():
                if value[0] <= int(note) < value[1]:
                    result_file.write(note.strip() + " " + key + "\n")
                    break

def exercice4(recipes_path):
    file_extension = path.splitext(recipes_path)[1]
    
    recipes = {}
    if path.exists(recipes_path):
        if file_extension == ".p":
            with open(recipes_path, 'rb') as f:
                # Exemple d'utilisation avec Pickle
                recipes = pickle.load(f)
        elif file_extension == ".json":
            with open(recipes_path, 'r') as f:
                # Ou en JSON si on veut garder la lecture en texte
                recipes = json.load(f)
        else:
            print(f"Format de fichier {file_extension} inconnu.")
            return

    recipes = run_interactive()

    if file_extension == ".p":
        with open(recipes_path, 'wb') as f:
            # Exemple d'utilisation avec Pickle
            pickle.dump(recipes, f)
    elif file_extension == ".json":
        with open(recipes_path, 'w') as f:
            # Ou en JSON si on veut garder la lecture en texte
            json.dump(recipes, f, indent=2)

def exercice5(file_path):
    with open(file_path, encoding="utf-8") as f:
        words = f.read().strip().split()

    number = [float(w) for w in words if w.isnumeric()]

    return sorted(number)

def exercice6(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        for index, line in enumerate(f1):
            if not index % 2:
                f2.write(line)


if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    exercice1("data/exemple.txt", "data/exemple2.txt")
    exercice2("data/exemple.txt", "output/exemple_copy.txt")
    exercice3("data/notes.txt", "data/seuils.json", "output/notes_letter.txt")
    exercice4("data/recettes.json")
    print(exercice5("data/exemple.txt"))
    exercice6("data/notes.txt", "output/notes_skip.txt")

