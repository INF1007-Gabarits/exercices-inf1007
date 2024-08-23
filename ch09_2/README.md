# Exemples en classe (chapitre 9)

## Logging (*logging_ex.py*)

Porte sur les slides 8 à 10 des notes du chapitre 9

## Exceptions (*exceptions_ex.py*)

Porte sur les slides 15 à 19 des notes du chapitre 9

## Tests unitaires (*tests_ex.py* et *code_to_test.py*)

Porte sur les slides 20 à 24 des notes du chapitre 9

## Ligne de commande (*code_to_test.py*)

Porte sur la slide 51 des notes du chapitre 9

## Documentation

Porte sur les slides 44 à 52 des notes du chapitre 9.

Après avoir écrit votre documentation dans votre code, vous pouvez générer un site web léger dans lequel la lire, un peu comme la documentation de Python ou celle des différentes librairies tierces.

Un des formats les plus courants ces temps-ci est le format [Sphinx](https://www.sphinx-doc.org/en/master/index.html). Pour s'en servir, on doit suivre quelques étapes :

1. Installer Make avec [`apt-get install build-essential`](https://packages.ubuntu.com/xenial/build-essential) sur Ubuntu, avec [MSYS2](https://www.msys2.org/) sur Windows ou avec [Homebrew](https://brew.sh/) sur Mac.
2. Installer sphinx avec `pip install sphinx` (probablement déjà installé).
3. Créer un dossier *doc* ou *docs* (ou peu importe comment vous voulez l'appeler) dans votre dossier de projet. On va dire *doc* pour le reste.
4. Dans ce dossier, faire `sphinx-quickstart --ext-autodoc` et choisir de séparer les sources.
5. Dans doc/source/conf.py, décommenter le code de la section *Path setup*. Dans le `sys.path`, ajouter le chemin vers les modules de votre projet (dans notre cas `../../`). Le squelette fait déjà les conversions pour vous, vous n'avez qu'à changer le chemin.
6. Pour ne pas avoir à ajouter à la main chaque fichier de votre projet, aller dans le dossier *doc* et faites `sphinx-apidoc -o source <chemin-vers-projet>`, où `<chemin-vers-projet>` est `../` dans notre cas, c'est-à-dire le chemin vers votre code Python. Faites cette étape quand vous ajoutez ou retirez des fichiers sources.
7. Faites `make html` dans le dossier *doc* pour générer la documentation. Elle sera dans *doc/build/html* (ouvrez le fichier *index.html*)
