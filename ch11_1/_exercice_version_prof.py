from game import *
from _character_version_prof import *


def main():
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmör", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()
