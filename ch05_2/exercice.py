#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	exit = "" + "\n"
	TAX_RATE = 0.14975

	sousTotal = 0
	for achat in data :
		affichage = achat[INDEX_NAME] + "\t" + str(achat[INDEX_QUANTITY] * achat[INDEX_PRICE]) + " $\n"
		exit += affichage

		sousTotal += achat[INDEX_QUANTITY] * achat[INDEX_PRICE]
	
	taxes = TAX_RATE * sousTotal
	total = sousTotal + taxes
	
	exit += "SOUS-TOTAL    " + str(round(sousTotal, 2)) + " $\n"
	exit += "TAXES         " + str(round(taxes, 2)) + " $\n" 
	exit += "TOTAL         " + str(round(total, 2)) + " $\n"

	return exit

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	return ""


def format_number(number, num_decimal_digits):
	posPoint = 0
	numberStr = str(abs(number))
	
	for i in range(len(numberStr)) :
		if numberStr[i] == "." :
			posPoint = i
	
	wholePart = numberStr[ : posPoint]
	fractionnaryPart = numberStr[posPoint + 1 : posPoint + 1 + num_decimal_digits]

	reversed_part = wholePart[ : : -1]
	formatted = ""
	for i in range(len(wholePart)) :
		for i in range(len(reversed_part)) :
			if i > 0 and i % 3 == 0 :
				formatted += " "
			formatted += reversed_part[i]
	
	wholePart = formatted[ : : -1]

	return str(wholePart) + "." + str(fractionnaryPart)

def format_number(number, num_decimal_digits):
	wholePart = int(abs(number))
	fractionnaryPart = abs(number) % 1

	wholePartStr = ""

	while wholePart >= 1000 :
		wholePart = number % 1000
		wholePartStr = str(wholePart) + wholePartStr

	return str(wholePart) + "." + str(fractionnaryPart)

def get_triangle(num_rows):
	LETTER = "A"
	exit = "+" * (2*num_rows + 1) + "\n"

	for n in range(0, num_rows) :
		lettersRow = (2*n + 1) * LETTER
		spaces = (num_rows - n - 1) * " "
		row = "+" + spaces + lettersRow + spaces + "+\n"
		exit += row

	exit += "+" * (2*num_rows + 1)
	return exit


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
