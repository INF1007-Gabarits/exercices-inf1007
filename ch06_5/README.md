[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Vérifications de balises de style HTML (chapitre 6)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indications contraires, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Réchauffement
### `check_brackets`

Vérifiez les fermetures dans un texte. Les parenthèses sont un exemple de fermeture. On veut dire n'importe-quel caractère d'ouverture et de fermeture qui sont passés en 2e paramètre de la fonction sous forme d'un tuple (ou d'une liste) de la forme `("ouverture1", "fermeture1", "ouverture2", "fermeture2")`. Par exemple si on vérifie les parenthèses (`(` avec `)`) et les accolades (`{` avec `}`). On aurait le tuple `("(", ")", "{", "}")`. On retourne vrai si les fermetures sont bonnes, faux sinon.

Exemple :
```python
brackets = ("(", ")", "{", "}")
yeet = "(yeet){yeet}"
yeeet = "({yeet})"
yeeeet = "({yeet)}"
yeeeeet = "(yeet"
print(check_brackets(yeet, brackets))
print(check_brackets(yeeet, brackets))
print(check_brackets(yeeeet, brackets))
print(check_brackets(yeeeeet, brackets))
```
Résultat :
```
True
True
False
False
```

## 2. Élimination des commentaires
### `remove_comments`

Enlevez les commentaires d'un texte à l'aide de balises d'ouverture et de fermeture spécifiées en paramètre. Si les commentaires sont mal formés, on retourne `None`.

Exemple :
```python
spam = "Hello, /* OOGAH BOOGAH */world!"
eggs = "Hello, /* OOGAH BOOGAH world!"
parrot = "Hello, OOGAH BOOGAH*/ world!"
print(remove_comments(spam, "/*", "*/"))
print(remove_comments(eggs, "/*", "*/"))
print(remove_comments(parrot, "/*", "*/"))
```
Résultat :
```
Hello, world!
None
None
```

## 3. Identification d'une balise au début d'un texte
### `get_tag_prefix`

Trouvez si une string commence par une balise d'ouverture ou de fermeture. Les balises sont passées en paramètres sous formes de deux tuples (ou listes). Si la string commence par une balise d'ouverture, on retourne `(la_balise, None)`, si elle commence par une balise de fermeture, on retourne `(None, la_balise)`, sinon on retourne `(None, None)`.

Exemple :
```python
otags = ("<head>", "<body>", "<h1>")
ctags = ("</head>", "</body>", "</h1>")
print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
print(get_tag_prefix("</h1></body>", otags, ctags))
print(get_tag_prefix("</body>", otags, ctags))
```
Résultat :
```
('<body>', None)
('<h1>', None)
(None, None)
(None, '</h1>')
(None, '</body>')
```

## 4. Vérification des balises d'un HTML restreint
### `check_tags`

Vérifiez que les balises d'un fichier de style HTML simplifié sont bien fermées. Les noms des balises sont passées en paramètre, mais sans les chevrons (donc "html", "head" par exemple). On doit enlever les commentaires, mais on ignore toutes les balises vides telles que `<br>` ou `<head/>`. On ne vérifie pas le `DOCTYPE` non plus. On s'en tient vraiment justes aux balises ouvrantes et fermantes. On retourne vrai si les fermetures sont bonnes, faux sinon.

Syntaxe HTML de base (pour référence) : https://www.tutorialrepublic.com/html-tutorial/html-elements.php

Exemple :
```python
spam = (
    "<html>"
    "  <head>"
    "    <title>"
    "      <!-- Ici j'ai écrit qqch -->"
    "      Example"
    "    </title>"
    "  </head>"
    "  <body>"
    "    <h1>Hello, world</h1>"
    "    <!-- Les tags vides sont ignorés -->"
    "    <br>"
    "    <h1/>"
    "  </body>"
    "</html>"
)
tags = ("html", "head", "title", "body", "h1")
comment_tags = ("<!--", "-->")
print(check_tags(spam, tags, comment_tags))
```
Résultat :
```
True
```

