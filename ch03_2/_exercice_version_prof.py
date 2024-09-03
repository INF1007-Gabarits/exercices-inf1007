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
	dollars = int(value)
	cents = int(round(value % 1.0 * 100 / 5) * 5)

	twenties = dollars // 20
	dollars %= 20
	tens = dollars // 10
	dollars %= 10
	fives = dollars // 5
	dollars %= 5
	ones = dollars

	quarters = cents // 25
	cents %= 25
	dimes = cents // 10
	cents %= 10
	nickels = cents // 5

	return twenties, tens, fives, ones, quarters, dimes, nickels;

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	# POUR CHAQUE v DANS values FAIRE
	sum = num_elems = 0
	for v in values:
		if v >= 0:
			sum += v
			num_elems += 1
	return sum / num_elems

def format_base(value, base, letters):
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base
		result += letters[digit_value]
		abs_value //= base
	if value < 0:
		result += "-"
	return result[::-1]


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(average([1, 4, -2, 10]))
	print(format_base(42, 16, "0123456789ABCDEF"))
