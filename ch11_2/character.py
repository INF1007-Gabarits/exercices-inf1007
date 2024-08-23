"""
Chapitre 11

Classes pour représenter un personnage.
"""


import utils
from abc import ABC, abstractmethod


class Move(ABC):
	"""
	Une action dans le jeu. Move.use doit être implémentée dans les classes dérivées

	:param name:      Le nom de l'action.
	:param min_level: Le niveau minimal pour l'utiliser.
	
	:ivar user: L'utilisateur actuel de l'action. Peut être utiliser dans les méthodes (self.user) pour accéder au personnage qui utilise cette action
	"""
	
	def __init__(self, name, min_level):
		self.__name = name
		self.min_level = min_level
		self.user = None

	@property
	def name(self):
		return self.__name

	def is_usable_by(self, character):
		return character.level >= self.min_level

	@abstractmethod
	def use(self, opponent):
		"""
		Cette méthode est appelée à chaque fois qu'un personnage utilise le move. Elle doit être réimplémentée par les classes dérivées.
		
		:param opponent: L'adversaire du personnage faisant le move.
		
		:returns: Un message (str) qui décrit succinctment ce qui s'est produit.
		"""
		pass

	def on_combat_begin(self):
		"""
		Cette méthode est appelée au début d'un combat entre deux personnages. Elle est appelée une fois sur tous les moves des deux personnages impliqués dans le combat.
		"""
		pass

	def on_turn_begin(self):
		"""
		Cette méthode est appelée au début de chaque tour d'un combat. Elle est appelée une fois sur tous les moves des deux personnages impliqués dans le combat, même si ce move n'a pas été utilisé. Elle est appelée avant que les personnages choisissent et effectuent leur action pour le tour.
		
		:returns: Un message (str) qui décrit succinctment ce qui s'est produit. Optionnel et peut être None.
		"""
		return None

class SimpleDamagingMove(Move):
	"""
	Une action infligeant du dommage direct à un adversaire.
	
	:param name:      Le nom de l'action.
	:param power:     La puissance de l'action.
	:param min_level: Le niveau minimal pour l'utiliser.
	"""

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		super().__init__(name, min_level)
		self.power = power

	def use(self, opponent):
		damage, crit = self.compute_damage(opponent)
		msg = self.apply_damage(opponent, damage, crit)
		return msg

	def apply_damage(self, opponent, damage, crit):
		opponent.hp -= damage
		msg = "  "
		if crit:
			msg += "Critical hit! "
		msg += f"{opponent.name} took {damage} dmg"
		return msg

	def compute_damage(self, opponent):
		return utils.compute_std_damage_output(
			self.user.level,
			self.power,
			self.user.attack,
			opponent.defense,
			1/16,
			(0.85, 1.00)
		)

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed Attack", cls.UNARMED_POWER, 1)

class Character:
	"""
	Un personnage dans le jeu

	:param name:    Le nom du personnage
	:param max_hp:  HP maximum
	:param attack:  Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level:   Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.__max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.__moves = [SimpleDamagingMove.make_unarmed(), None, None]
		self.unarmed_attack.user = self
		self.hp = max_hp

	@property
	def name(self):
		return self.__name

	@property
	def max_hp(self):
		return self.__max_hp

	@max_hp.setter
	def max_hp(self, value):
		self.__max_hp = value
		self.hp = self.hp

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = round(utils.clamp(val, 0, self.max_hp))

	@property
	def unarmed_attack(self) -> SimpleDamagingMove:
		return self.__moves[0]

	@property
	def main_move(self) -> Move:
		return self.__moves[1]

	@main_move.setter
	def main_move(self, value):
		self._set_move(1, value)
		
	@property
	def secondary_move(self) -> Move:
		return self.__moves[2]

	@secondary_move.setter
	def secondary_move(self, value):
		self._set_move(2, value)

	@property
	def moves(self):
		return tuple(self.__moves)

	def use_move(self, index, opponent):
		if index not in (0, 1, 2):
			raise IndexError(index)
		
		if self.__moves[index] is None:
			return f"{self.name} just stares blankly"
		msg = f"{self.name} used {self.__moves[index].name}\n"
		use_msg = self.__moves[index].use(opponent)
		msg += self._format_use_msg(use_msg)
		return msg

	def _set_move(self, index, value):
		if index not in (1, 2):
			raise IndexError(index)
		
		if value is not None and not value.is_usable_by(self):
			raise ValueError(f"{value.name} is not usable by {self.name}")
		self.__moves[index] = value
		self.__moves[index].user = self
	
	@staticmethod
	def _format_use_msg(use_msg):
		return "  " + use_msg.strip().replace("\n", "\n  ")
		

