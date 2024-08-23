"""
Classes d'actions magiques
"""


from character import *


# On veut créer une action qui cause du dommage à un adversaire et qui restaure une portion de ce dommage à l'attaquant. On a déjà une classe qui inflige du dommage directement, on va donc en hériter et ajuster l'exécution de sa méthode use.
class DrainingMove(...): # TODO: Hériter de la bonne classe
	"""
	Applique du dommage normalement à un adversaire et restaure une partie de ce dommage en HP à l'utilisateur du move.
	
	:param name:         Le nom de l'action.
	:param power:        La puissance de l'action.
	:param drain_factor: La proportion des HP de dommage qui sont restaurés.
	:param min_level:    Le niveau minimal pour l'utiliser.
	"""

	# TODO: Le __init__ qui initialise la classe de base et l'attribut drain_factor

	# TODO: Surcharger la méthode `use` pour appliquer le dommage en réutilisant les méthodes de la classe de base. Il faut ensuite restaurer les points absorbés. HP restaurés = dommage * draining_factor

# On veut une action qui gagne en puissance à mesure que le combat avance, donc à chaque tour.
class IntensifyingMove(...): # TODO: Hériter de la bonne classe
	"""
	Applique du dommage normalement à un adversaire et restaure une partie de ce dommage en HP à l'utilisateur du move.
	
	:param name:            Le nom de l'action.
	:param power:           La puissance de l'action.
	:param bonus_increment: Le bonus de dommage cumulatif qui est gagné à chaque tour
	:param min_level:       Le niveau minimal pour l'utiliser.
	
	:ivar current_bonus: Le bonus accumulé depuis le début du combat.
	"""
	
	# TODO: Le __init__ qui initialise la classe de base et l'attribut bonus_increment. On créer aussi un attribut `current_bonus` qui compte le bonus actuel
	# TODO: Surcharger la méthode `on_combat_begin` qui remet `current_bonus` à 0.

	# TODO: Surcharger la méthode `on_turn_begin` qui ajoute `bonus_increment` à `current_bonus`.

	# TODO: Surcharger la méthode `compute_damage` qui réutilise la version de la classe de base en lui ajoutant le bonus accumulé.

