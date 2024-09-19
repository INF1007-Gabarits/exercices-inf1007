# Exercices en vrac (chapitre 5)

À moins d'indication contraire, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Facture

On a la liste des achats fait par un client. La liste des achats est une liste de tuples dont les éléments sont le nom de l'article, sa quantité et son prix unitaire. Par exemple :

```python
achats = [
    ("chaise ergonomique", 1, 399.99),
    ("g-fuel", 69, 35.99),
    ("blue screen", 2, 39.99)
]
```

On veut formater une facture avec la liste des items et le total. On veut un formatage qui aligne les éléments avec des espaces.

```
chaise ergonomique     399.99 $
g-fuel                2483.31 $
blue screen             79.98 $
- - - - - - - - - - - - - - - - -
SOUS TOTAL    2963.28 $
TAXES          444.49 $
TOTAL         3407.77 $
```

### 1.1 Total avec taxes

Formater la dernière partie d'une facture à partir de liste des achats d'un client. La facture doit afficher le sous-total, le montant des taxes et le total avec taxes en supposant un taux de 15% de taxes. Les montants dans la facture doivent être écrits alignés à droite sur 10 colonnes et avoir deux chiffres décimaux suivi d’un signe de dollar. Il faut suivre le format de l’exemple.

Si on a comme entrée :
```python
achats = [
    ("chaise ergonomique", 1, 399.99),
    ("g-fuel", 69, 35.99),
    ("blue screen", 2, 39.99)
]
```
La sortie de `print(format_bill_total(achats))` devrait être :
```
SOUS TOTAL    2963.28 $
TAXES          444.49 $
TOTAL         3407.77 $
```

### 1.2 Liste des prix d'items

Formater la liste des items avec un item par ligne. Chaque ligne a le nom de l'item puis son coût (qté × prix unit.). Le nom de l'article doit être aligné sur la longueur maximale des noms de la liste. Les montants dans la facture doivent être écrits alignés à droite sur 10 colonnes et avoir deux chiffres décimaux suivi d’un signe de dollar.

Par exemple, si on a comme entrée :
```python
achats = [
    ("chaise ergonomique", 1, 399.99),
    ("g-fuel", 69, 35.99),
    ("blue screen", 2, 39.99)
]
```
La sortie de `print(format_bill_items(achats))` devrait être :
```
chaise ergonomique     399.99 $
g-fuel                2483.31 $
blue screen             79.98 $
```

Cependant, l'entrée : 
```python
achats = [
    ("g-fuel", 69, 35.99),
    ("blue screen", 2, 39.99)
]
```
Nous donnerait plutôt la sortie :
```
g-fuel         2483.31 $
blue screen      79.98 $
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
