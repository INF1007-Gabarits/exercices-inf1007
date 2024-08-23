"""
Classes d'actions magiques
"""


from character import *


# On veut créer une action qui cause du dommage à un adversaire et qui restaure une portion de ce dommage à l'attaquant. On a déjà une classe qui inflige du dommage directement, on va donc en hériter et ajuster l'exécution de sa méthode use.
class DrainingMove(SimpleDamagingMove):
	"""
	Applique du dommage normalement à un adversaire et restaure une partie de ce dommage en HP à l'utilisateur du move.
	
	:param name:         Le nom de l'action.
	:param power:        La puissance de l'action.
	:param drain_factor: La proportion des HP de dommage qui sont restaurés.
	:param min_level:    Le niveau minimal pour l'utiliser.
	"""

	def __init__(self, name, power, drain_factor, min_level):
		# On réutilise le __init__ de SimpleDamagingMove.
		super().__init__(name, power, min_level)
		# On initialise l'attribut.
		self.drain_factor = drain_factor

	def use(self, opponent):
		# On réutilise les méthodes de SimpleDamagingMove pour calculer et appliquer le dommage.
		damage, crit = self.compute_damage(opponent)
		msg = self.apply_damage(opponent, damage, crit)
		
		# On calcule et applique les HP restorés et on l'ajoute au message déjà construit par l'étape précédente.
		heal = round(damage * self.drain_factor)
		self.user.hp += heal
		msg += f"\n{self.user.name} healed {heal} HP"
		
		return msg

# On veut une action qui gagne en puissance à mesure que le combat avance, donc à chaque tour.
class IntensifyingMove(SimpleDamagingMove):
	"""
	Applique du dommage normalement à un adversaire et restaure une partie de ce dommage en HP à l'utilisateur du move.
	
	:param name:            Le nom de l'action.
	:param power:           La puissance de l'action.
	:param bonus_increment: Le bonus de dommage cumulatif qui est gagné à chaque tour.
	:param min_level:       Le niveau minimal pour l'utiliser.
	
	:ivar current_bonus: Le bonus accumulé depuis le début du combat.
	"""

	def __init__(self, name, power, bonus_increment, min_level):
		# On réutilise le __init__ de SimpleDamagingMove.
		super().__init__(name, power, min_level)
		# On initialise l'incrément de puissance.
		self.bonus_increment = bonus_increment
		# On crée un attribut pour accumuler le bonus.
		self.current_bonus = 0

	def on_combat_begin(self):
		# À chaque début de combat, on réinitialise le bonus actuel.
		self.current_bonus = 0

	def on_turn_begin(self):
		# On ajoute bonus_increment au bonus actuel.
		self.current_bonus += self.bonus_increment
		return f"{self.user.name}'s {self.name} has {self.current_bonus}"

	def compute_damage(self, opponent):
		# On calcule le dommage en réutilisant la version de base, puis on lui ajoute le bonus.
		base_damage, crit = super().compute_damage(opponent)
		damage = base_damage + self.current_bonus
		return damage, crit

class HealingMove(Move):
	"""
	Restaure un certain pourcentage du HP max de son utilisateur à chaque début de tour pour un certain nombre de tours
	
	:param name:           Le nom de l'action.
	:param healing_factor: La proportion (entre 0 et 1) du max HP restaurée à chaque tour.
	:param num_turns:      Le nombre de tours actifs.
	:param min_level:      Le niveau minimal pour l'utiliser.
	
	:ivar num_remaining_active_turns: Le nombre de tours de guérison actifs restant.
	"""

	def __init__(self, name, healing_factor, num_turns, min_level):
		# On réutilise le __init__ de Move.
		super().__init__(name, min_level)
		# On initialise les attributs 
		self.healing_factor = healing_factor
		self.num_turns = num_turns
		self.remaining_active_turns = 0

	def use(self, opponent):
		self.remaining_active_turns = self.num_turns
		return f"{self.user.name} will be healing for the next {self.num_turns} turns"

	def on_combat_begin(self):
		self.remaining_active_turns = 0

	def on_turn_begin(self):
		if self.remaining_active_turns > 0:
			self.remaining_active_turns -= 1
			return self.apply_healing()

	def apply_healing(self):
		healing = round(self.healing_factor * self.user.max_hp)
		self.user.hp += healing
		return f"{self.user.name} was healed for {healing} HP"
