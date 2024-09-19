#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	power = voltage**2 / resistance
	return power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	# v1[0] et v2[0] pour accéder au X
	# v1[1] et v2[1] pour accéder au Y

	dot_product = v1[0] * v2[0] + v1[1] * v2[1]
	return dot_product == 0

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y

	distance_x = circle_center[0] - point[0]
	distance_y = circle_center[1] - point[1]
	distance = math.sqrt(distance_x**2 + distance_y**2)
	return distance <= circle_radius

def cash(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près.

	# Partie entière (les dollars).
	dollars = int(value)
	# Partie décimale fois 100 (donc les cents) et arrondie au multiple de 5 le plus proche. Ça nous permet de faire le traitement des cents avec des entiers (plus simple et efficace).
	cents = int(round(value % 1.0 * 100 / 5) * 5)

	# Les dénominations pour les dollars.
	twenties = dollars // 20
	dollars %= 20
	tens = dollars // 10
	dollars %= 10
	fives = dollars // 5
	dollars %= 5
	ones = dollars

	# Les dénominations pour les cents.
	quarters = cents // 25
	cents %= 25
	dimes = cents // 10
	cents %= 10
	nickels = cents // 5

	# Retourner les valeurs dans un tuple (oui on peut faire ça).
	return twenties, tens, fives, ones, quarters, dimes, nickels;

def format_base(value, base, letters):
	# Commencer par une string vide.
	result = ""
	# Traiter seulement la valeur absolue pour simplifier (on ajoute de signe de négation plus tard)
	abs_value = abs(value)
	# Tant qu'il reste des chiffres à traiter :
	while abs_value != 0:
		# Extraire le prochain chiffre dans la base donnée
		digit_value = abs_value % base
		# Ajouter à la fin du résultat le caractère du chiffre en question.
		result += letters[digit_value]
		# « Tasser à droite » la valeur restante de la base donnée pour passer au prochain chiffre.
		abs_value //= base
	# Ajouter le signe de négation si le nombre original est négatif
	if value < 0:
		result += "-"
	# À ce moment, on a la bonne string, mais à l'envers, donc on la retourne renversée.
	# Utiliser un pas négatif dans le slicing part de la fin plutôt que du début, donc [::-1] prend la string au complet, mais en partant de la fin, donc la string renversée.
	return result[::-1]

	# Approche alternative : on aurait pu faire result = letters[digit_value] + result, puis mettre le signe de négation au début plutôt qu'à la fin de la string sans faire le renversement. Ça revient au même.


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-420, 16, "0123456789ABCDEF"))
