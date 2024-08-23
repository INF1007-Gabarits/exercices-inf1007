def add_recipes(dictionnaire):
    name = input("Entrez le nom de votre recette?\n")
    ingredients = input("Entrez la liste d'ingrédients de la recette, svp séparer les ingrédients par une ,\n").split(",")
    ingredients = [ing.strip() for ing in ingredients]
    dictionnaire[name] = ingredients

    return dictionnaire

def delete_recipe(dictionary):
    name = input("Entrez le nom de la recette que vous voulez supprimer.\n")

    if name in dictionary:
        del dictionary[name]
        print("La recette est supprimée!")
    else:
        print("Cette recette n'existe pas!")

    return dictionary

def print_recipe(ingredients):
    name = input("Entrez le nom d'une recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("La recette demandée n'existe pas!")
        print(f"Les recettes existantes sont: {list(ingredients.keys())}")

def run_interactive(recipes):
    while True:
        choice = input(
            "Choisissez une option: \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette \n d) Afficher une recette \n e) Quitter le programme\n").strip().lower()

        if choice == "a":
            recipes = add_recipes(recipes)
        elif choice == "b":
            recipes = add_recipes(recipes)
        elif choice == "c":
            recipes = delete_recipe(recipes)
        elif choice == "d":
            print_recipe(recipes)
        elif choice == "e":
            break
        else:
            print("L'option choisi n'est pas valide!")

    return recipes
