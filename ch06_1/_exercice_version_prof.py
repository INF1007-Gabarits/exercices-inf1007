#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: Demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Please enter a value\n"))

    num_values = [float(value) for value in values if value.isdigit()]
    str_values = [value for value in values if not value.isdigit()]

    return sorted(num_values) + sorted(str_values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        words = []
        while len(words) < 2:
            words.append(input("Please enter string\n"))

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:

    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        average = sum(value)/len(value)

        if len(best_student) == 0 or list(best_student.values())[0] < average:
            best_student = {key: average}

    return best_student



def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"Le caractère {key} revient {frequency[key]} fois.")

    return frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données
    name = input("Quel est le nom de votre recette?\n")
    ingredient = input("Entrer la liste d'ingrédients? Séparer les ingrédiants par une ,\n").split(",")

    return {name: ingredient}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Quel est le nom de votre recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("Cette recette n'est pas dans le livre!")
        print_recipe(ingredients)



def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
