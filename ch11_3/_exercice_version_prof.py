"""
Chapitre 11.2
"""


import math

from _matrix_version_prof import *


def main():
	foo = Matrix(2, 3)
	foo[0, 0] = 69.1
	foo[0, 2] = 69.2
	print(foo[0, 0])
	print(foo[0, 2])
	print(foo.data)

	print("-" * 40)

	foo = Matrix(2, 3, [
		11, 12, 13,
		21, 22, 23
	])
	print(foo)
	print(repr(foo))

	print("-" * 40)

	foo = Matrix(2, 3, [
		1.1, 1.2, 1.3,
		2.1, 2.2, 2.3
	])
	print(format(foo, "5.2f"))
	print(f"{foo :5.2f}")

	print("-" * 40)

	foo = Matrix(2, 3, [
		1.1, 1.2, 1.3,
		2.1, 2.2, 2.3
	])
	print(-foo)

	print("-" * 40)

	foo = Matrix(2, 3, [
		1.0, 1.0, 1.0,
		2.0, 2.0, 2.0
	])
	bar = Matrix(2, 3, [
		0.1, 0.2, 0.3,
		0.1, 0.2, 0.3
	])
	print(foo + bar)
	print()
	print(foo - bar)

	print("-" * 40)

	foo = Matrix(2, 3, [
		11, 12, 13,
		21, 22, 23
	])
	bar = Matrix(3, 2, [
		11, 12,
		21, 22,
		31, 32
	])
	print(foo * bar)
	print()
	print(foo * 10)

	print("-" * 40)
	
	foo = Matrix(2, 3, [
		11, 12, 13,
		21, 22, 23
	])
	bar = Matrix(3, 2, [
		11, 12,
		21, 22,
		31, 32
	])
	qux = Matrix(2, 3, [
		11, 12, 13,
		21, 22, 23
	])
	print(foo == bar)
	print(foo == foo)
	print(foo == qux)
	print(foo != bar)

if __name__ == "__main__":
	main()

