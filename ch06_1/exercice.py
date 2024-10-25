#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    nbValues = int(input("Nombre de valeurs ? "))
    if values is None :
        for i in range(nbValues) :
            values.append(float(input("n" + (i + 1) + " = ")))
    
    sorted = False
    found = False
    for i in range(len(1, values + 1)) :
        pass

    return []


def anagrams(words: list = None) -> bool:
    if words is None:
        while len(word) > 2 :
            words.append(input("Entrer un mot. "))

    slices = []
    for word in words :
        slices.append(sorted(word))

    anagram = False
    found = False
    for i in range(1, len(slices) + 1) :
        if False :
            pass

    return False


def contains_doubles1(items: list) -> bool:
    ensemble = set(items)
    return len(ensemble) != len(items)

def contains_doubles(items: list) -> bool:
    containsDouble = False

    for elem in items :
        if items.count(elem) > 1 and (not containsDouble) :
            containsDouble = True

    return containsDouble


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    bestStudent = dict()
    bestMean = 0
    
    for nom, notes in student_grades.items() :
        moy = moyenne(notes)

        if moy > bestMean :
            bestMean = moy
            bestStudent = {nom : moy}

    return bestStudent

def moyenne(liste) -> float :
    somme = 0
    longueur = 0

    for elem in liste :
        somme += elem
        longueur += 1
    
    return somme/longueur

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    freq = {}

    for char in sentence :
        freq[char] = sentence.count(char)

    sortedFreqs = sorted(freq, key = freq.__getitem__, reverse = True)
    TIMES_WANTED = 5
    for key in sortedFreqs :
        if freq[key] > TIMES_WANTED :
            print(f"Le caractère {key} revient {freq[key]} fois.")

    return sortedFreqs


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recipe = input("Entrez une recette.\t")
    ingredients = []
    hasFinished = False
    count = 0

    while not hasFinished :
        count += 1
        ingredients.append(input("Entrez l'ingrégient #" + str(count) + " de la recette.\t"))

        end = input("Souhaitez-vous continuer (O/N) ?\t")
        if end == "O".lower() :
            hasFinished = False
        elif end == "N" :
            hasFinished = True

    return {recipe : ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recipe = input("Entrez une recette.\t")

    if recipe in ingredients :
        print(ingredients[recipe])
    else :
        print("Cette recette n'est pas dans le livre !")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    #order()

    print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83], "Stéphane" : [95, 99, 100]}
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
