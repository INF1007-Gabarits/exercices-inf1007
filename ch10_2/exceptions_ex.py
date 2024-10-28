from math import sqrt
import sys
import logging


def is_prime(num):
	for i in range(2, int(round(sqrt(num))) + 1):
		if num % i == 0:
			return False
	return True

def prime_factors(num):
	for i in range(2, int(num / 2) + 1):
		if is_prime(i) and num % i == 0:
			yield i

def read_int_from_stdin():
	input_line = input("Entrez un nombre entier positif supérieur à 3 : ")
	logging.debug(f"Entered '{input_line}'")
	num = int(input_line)
	if num <= 3:
		raise ValueError()
	return num, input_line


def main():
	logging.basicConfig(
		filename="logs/num.log",
		format="[%(asctime)s] %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S",
		level=logging.DEBUG
	)

	while True:
		try:
			num, input_line = read_int_from_stdin()
		except ValueError:
			print("Le nombre entré n'est pas un entier > 3. bruh.")
		except KeyboardInterrupt:
			print("\n" "Ok ok on va s'arrêter là. Calme tes nerfs mon dude.")
			input_line = "<KeyboardInterrupt>"
			return
		else:
			print("Ok c'est beau on continue...")
			break

	print("Les facteurs premiers sont : ", end="")
	for fac in prime_factors(num):
		print(fac, end=" ")
	print()

if __name__ == "__main__":
	main()
