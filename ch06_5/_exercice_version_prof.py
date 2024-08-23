#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	# TODO: Associer les ouvrantes et fermantes (à l'aide d'un dict)
	opening_brackets = dict(zip(brackets[0::2], brackets[1::2])) # Ouvrants à fermants
	closing_brackets = dict(zip(brackets[1::2], brackets[0::2])) # Fermants à ouvrants

	# TODO: Vérifier les ouvertures/fermetures
	bracket_stack = []
	# Pour chaque char de la string
	for chr in text:
		# Si ouvrant:
		if chr in opening_brackets:
			# On empile
			bracket_stack.append(chr)
		# Si fermant
		elif chr in closing_brackets:
			# Si la pile est vide ou on n'a pas l'ouvrant associé au top de la pile
			if len(bracket_stack) == 0 or bracket_stack[-1] != closing_brackets[chr]:
				# Pas bon
				return False
			# On dépile
			bracket_stack.pop()
	# On vérifie que la pile est vide à la fin (au cas où il y aurait des ouvrants de trop)
	return len(bracket_stack) == 0

def remove_comments(full_text, comment_start, comment_end):
	# Cette ligne sert à rien, on ne modifie pas la variable originale de toute façon
	text = full_text
	while True:
		# Trouver le prochain début de commentaire
		start = text.find(comment_start)
		# Trouver la prochaine fin de commentaire
		end = text.find(comment_end)
		# Si aucun des deux trouvés
		if start == -1 and end == -1:
			return text
		# Si fermeture précède ouverture ou j'en ai un mais pas l'autre
		if end < start or (start == -1) != (end == -1):
			# Pas bon
			return None
		# Enlever le commentaire de la string
		text = text[:start] + text[end + len(comment_end):]

def get_tag_prefix(text, opening_tags, closing_tags):
	for otag, ctag in zip(opening_tags, closing_tags):
		if text.startswith(otag):
			return (otag, None)
		elif text.startswith(ctag):
			return (None, ctag)
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):
	text = remove_comments(full_text, *comment_tags)
	if text is None:
		return False

	# On construit nos balises à la HTML ("head" donne "<head>" et "</head>")
	opening_tags = {f"<{name}>": f"</{name}>" for name in tag_names} # Ouvrant à fermant
	closing_tags = dict((v, k) for k, v in opening_tags.items()) # Fermant à ouvrant

	# Même algo qu'au numéro 1, mais adapté aux balises de plusieurs caractères
	tag_stack = []
	while len(text) != 0:
		opening, closing = get_tag_prefix(text, opening_tags.keys(), closing_tags.keys())
		# Si ouvrant:
		if opening is not None:
			# On empile et on avance
			tag_stack.append(opening)
			text = text[len(opening):]
		# Si fermant:
		elif closing is not None:
			# Si pile vide OU match pas le haut de la pile:
			if len(tag_stack) == 0 or tag_stack[-1] != closing_tags[closing]:
				# Pas bon
				return False
			# On dépile et on avance
			tag_stack.pop()
			text = text[len(closing):]
		# Sinon:
		else:
			# On avance jusqu'à la prochaine balise.
			text = text[1:]
	# On vérifie que la pile est vide à la fin (au cas où il y aurait des balises ouvrantes de trop)
	return len(tag_stack) == 0

if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

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
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

