[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 5)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indication contraires, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Facture

Formater une facture à partir du nom d'un client et de la liste de ses achats. La liste des achats est une liste de tuples dont les éléments sont le nom de l'article, sa quantité et son prix unitaire. La facture doit afficher le nom du client, le sous-total, le montant des taxes et le total avec taxes en supposant un taux de 15% de taxes. Les montants dans la facture doivent être écrits sous le nom du client, être alignés à droite sur 10 colonnes et avoir deux chiffres décimaux suivi d’un signe de dollar. Il faut suivre le format de l’exemple.

Si on a comme entrée :
```
nom = "Äpik Gämmör"
achats = [
    ("chaise", 1, 399.99),
    ("g-fuel", 69, 35.99)
]
```
La sortie de `print(get_bill(nom, achats))` devrait être :
```
Äpik Gämmör
SOUS TOTAL    2883.30 $
TAXES          432.50 $
TOTAL         3315.80 $
```

## 2. Nombre formaté

Formatter un nombre passé en paramètre avec un nombre de chiffres décimaux aussi en paramètre et un espace séparant les groupes de trois chiffres. Faites la séparation des chiffres avec une boucle (pas avec les fonctions de string). Le nombre donné en paramètre peut être négatif.

Par exemple, le nombre 1456846.8946 avec trois chiffres décimaux vous donnerait la string `'1 456 846.895'`.

## 3. Triangle

Produire une string qui représente un triangle isocèle formé de la lettre `A` entouré par une bordure formée de la lettre `+`. La hauteur du triangle est passée en paramètre.

Par exemple, `print(get_triangle(2))` donne :
```
+++++
+ A +
+AAA+
+++++
```
`print(get_triangle(5))` donne :
```
+++++++++++
+    A    +
+   AAA   +
+  AAAAA  +
+ AAAAAAA +
+AAAAAAAAA+
+++++++++++
```

## Conseils et ressources

Spécifications des string formatées : https://docs.python.org/3/library/string.html#formatspec

Table des caractères d'échappement : https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
