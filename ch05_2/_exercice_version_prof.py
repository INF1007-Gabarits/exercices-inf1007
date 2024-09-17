#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	TAX_RATE = 0.15

	# Calculer le sous-total (somme des items)
	sum = 0
	for item in data:
		sum += item[INDEX_QUANTITY] * item[INDEX_PRICE]

	# Calculer les taxes et total
	taxes = TAX_RATE * sum
	total = sum + taxes

	# Retourner le bas de la facture formatée (sous-total, taxes, total)
	bill_data = [
		("SOUS TOTAL", sum),
		("TAXES     ", taxes),
		("TOTAL     ", total)
	]
	result = ""
	for bd in bill_data:
		result += f"{bd[0]} {bd[1]:>10.2f} $" "\n"

	# Approche avec répétition de code
	#result += f"SOUS-TOTAL {sum : >10.2f} $" "\n" 
	#result += f"TAXES      {taxes : >10.2f} $ "\n"
	#result += f"TOTAL      {total : >10.2f} $"

	return result

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	# Trouver la longueur maximale des noms d'item.
	max_length = 0
	for item in data:
		if len(item[INDEX_NAME]) > max_length:
			max_length = len(item[INDEX_NAME])

	# Pour chaque item, formater le nom sur la longueur maximale et le prix total (qté x prix) sur 10 caractère et 2 décimales.
	result = ""
	for item in data:
		result += f"{item[INDEX_NAME]:{max_length}} {item[INDEX_QUANTITY] * item[INDEX_PRICE]: >10.2f} $" "\n"

	return result

def format_number(number, num_decimal_digits):
	# Séparer les parties entière et décimale
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))

	# Formater la partie décimale
	decimal_str = str(int(round(decimal_part * 10**num_decimal_digits)))
	decimal_str = "." + decimal_str + "0" * (num_decimal_digits - len(decimal_str))
	# Approche plus automagique : decimal_str = f"{decimal_part:.{num_decimal_digits}f}"[1:]

	# Formater la partie entière
	whole_part_str = ""
	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part //= 1000
	whole_part_str = str(whole_part) + whole_part_str

	# Concaténer les deux parties
	return ("-" if number < 0 else "") + whole_part_str + decimal_str

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	# Calculer la largeur
	triangle_width = 1 + 2 * (num_rows - 1)

	# Construire première et dernière ligne (bordures pleines)
	border_row = BORDER_CHAR * (triangle_width + 2)

	# Afficher le triangle
	result = border_row
	# Pour chaque ligne du triangle
	for i in range(num_rows):
		triangle_chars = TRIANGLE_CHAR * (i * 2 + 1)
		result += "\n" + f"{BORDER_CHAR}{triangle_chars: ^{triangle_width}}{BORDER_CHAR}"
	result += "\n" + border_row

	return result


if __name__ == "__main__":
	purchases = [
		("chaise ergonomique", 1, 399.99),
		("g-fuel", 69, 35.99),
		("blue screen", 2, 39.99)
	]
	print(format_bill_items(purchases).strip())
	print("- - - - - - - - - - - - - - - - - - -")
	print(format_bill_total(purchases).strip())

	print("\n------------------")

	print(format_number(-1420069.0678, 2))

	print("\n------------------")

	print(get_triangle(2))
	print(get_triangle(5))
