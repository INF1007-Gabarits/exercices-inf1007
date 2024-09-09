# Exercices en vrac (chapitre 4)

À moins d'indication contraire, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Prénoms composés

Soit un prénom composé (avec un trait d’union) passé en paramètre (exemple « jean-luc »). Il faut extraire le premier prénom (exemple « jean » pour « jean-luc ») puis le mettre dans la phrase « Bonjour *PremierPrénom* » (exemple « Bonjour Jean »). La première lettre du prénom doit être en majuscule (même si le paramètre est en minuscule). Indice : Les chaînes de caractères possèdent des fonctions de recherche et de séparation.

## 2. Texte à trous

Bâtir la phrase «Aujourd’hui, j’ai vu un \<animal\> s’emparer d’un panier \<adjectif\> plein de \<fruit\>.» en sélectionnant aléatoirement l’animal, l’adjectif et le fruit à partir de ceux donnés en paramètres. Les paramètres sont trois tuples de n'importe quelle taille.

Par exemple si on a les animaux `(chevreuil, chien, pigeon)`, les adjectifs `(rouge, officiel, lourd)` et les fruits `(pommes, kiwis, bananes)`, on pourrait obtenir la phrase :
```
Aujourd’hui, j’ai vu un pigeon s’emparer d’un panier rouge plein de kiwis.
```

Pour générer des nombres aléatoires en Python, référez-vous à https://docs.python.org/3/library/random.html, spécifiquement aux fonctions pour les entiers.

## 3. Formater la date et l'heure

Prendre une date (année, mois, jour) et heure (heures, minutes, secondes) et la formater avec quatre chiffres pour l'années, deux chiffres pour le mois, jour, heures et minutes, et deux chiffres entiers et trois décimales pour les secondes. On sépare les éléments de la date par des traits et les éléments de l'heure par des deux-points. la date et l'heure est séparée par un espace.

Par exemple, le 12 janvier 1970 à 12h 30m 4.5678s nous donnerait la string `1970-01-12 12:30:04.568`. On remarque l'arrondi des fractions de seconde.

## 4. Code de César

Le chiffrement par décalage, aussi connu comme le chiffre de César ou le code de César est une méthode de chiffrement très simple utilisée par Jules César dans ses correspondances secrètes. Le texte chiffré s'obtient en remplaçant chaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet. Pour les dernières lettres (dans le cas d'un décalage à droite), on reprend au début. Par exemple avec un décalage de 3 vers la droite, A est remplacé par D, B devient E, et ainsi jusqu'à W qui devient Z, puis X devient A etc. La longueur du décalage, 3 dans l'exemple évoqué, constitue la clé du chiffrement qu'il suffit de transmettre au destinataire (tiré de [Wikipédia](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage)).

La fonction `encrypt` prend une chaîne de caractère et un décalage et retourne la chaîne cryptée avec ce décalage. Pour simplifier les opérations, la chaine retournée devrait être toute en majuscule. La fonction `decrypt` fait l'opération inverse. Ne cryptez que les caractères alphabétiques, tous les autres caractères (chiffres, espaces, ponctuation) restent les mêmes.

Par exemple:
```python
print(encrypt("ABC", 1))
print(encrypt("abc 123 XYZ", 3))
print(decrypt("DEF 123 ABC", 3))
```
Nous donne
```
BCD
DEFGHI
abc 123 DEF
```
