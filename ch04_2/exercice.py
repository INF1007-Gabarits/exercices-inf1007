#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	posChar = 0
	for i in range(len(name)) :
		if name[i] == "-" :
			posChar =  i
	
	firstName = name[:posChar].capitalize()
		
	return "Bonjour, " + firstName

def get_random_sentence(animals, adjectives, fruits):
	indexAnimals = random.randrange(len(animals))
	indexAdjectives = random.randrange(len(adjectives))
	indexFruits = random.randrange(len(fruits))
	sentence = "Aujourd’hui, j’ai vu un " + animals[indexAnimals] + " s’emparer d’un " + adjectives[indexAdjectives] +  " plein de " + fruits[indexFruits] + "."
	return sentence

def format_date(year, month, day, hours, minutes, seconds):
	yearStr = ""
	monthStr = ""
	dayStr = ""
	hoursStr = ""
	minutesStr = ""
	secondsStr = ""

	if len(str(year)) == 1 :
		yearStr = "0" + str(year)
	else :
		yearStr = str(year)

	if len(str(month)) == 1 :
		monthStr = "0" + str(month)
	else :
		monthStr = str(month)
	
	if len(str(day)) == 1 :
		dayStr = "0" + str(day)
	else :
		dayStr = str(day)
	
	if len(str(hours)) == 1 :
		hoursStr = "0" + str(hours)
	else :
		hoursStr = str(hours)
	
	if len(str(minutes)) == 1 :
		minutesStr = "0" + str(minutes)
	else :
		minutesStr = str(minutes)
	
	secondsStr = str(round(seconds, 3))

	date = yearStr + "-" + monthStr + "-" + dayStr + " " + hoursStr + ":" + minutesStr + ":" + secondsStr
	return date

def encrypt(text, shift):
	encryptedText = ""

	for char in text :
		if char == " " :
			encryptedText += " "
		else :
			encryptedText += chr(ord(char) + shift)
	
	return encryptedText

def decrypt(encrypted_text, shift):
	decryptedText = ""

	for char in encrypted_text :
		if char == " " :
			decryptedText += " "
		else :
			decryptedText += chr(ord(char) - shift)
	
	return decryptedText


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
