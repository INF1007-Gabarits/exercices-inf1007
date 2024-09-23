#!/usr/bin/env python

def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2 / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	return prodScalaire(v1, v2) == 0

def prodScalaire(a, b) :
	return a[0]*b[0] + a[1]*b[1]

def average(values) :
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme = 0
	qte = 0
	
	for val in values :
		if val <= 0 :
			somme += val
			qte += 1
		#else :
			# Valeur négative !! On la passe.
	
	moyenne = somme / qte
	return moyenne

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y
	distX = point[0] - circle_center[0]
	distY = point[0] - circle_center[0]
	dist = normeVect([distX, distY])
	
	return dist >= circle_radius

def normeVect(v) :
	norme = 0
	for i in range(len(v)) :
		norme += v[i]**2
	
	norme **= 1/2
	return norme

def bills(value) :
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur. 
	# Il faut remplir les variables twenties, tens, fives, twos et ones avec le quantité de chaque dénomination.
	bills = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05]
	values = []
	#qtyBills = []

	for i in range(len(bills)) :
		values.append(value//bills[i])
		value %= bills[i]

	return values
	#hundreds, fifties, twenties, tens, fives, twos, ones,  = values[0], values[1], values[2], values[3], values[4], values[5], values[6]
	#return (hundreds, fifties, twenties, tens, fives, twos, ones)

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0 :
		valeurChiffre = abs_value % base
		
	if value < 0 :
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result += "-"
	return result


if __name__ == "__main__" :
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-420, 16, "0123456789ABCDEF"))