"""
Chapitre 11.2
"""


import numbers
import copy


class DimensionsTypeError(TypeError):
	pass

class DimensionsError(ValueError):
	pass

class IncompatibleOperandsError(DimensionsError):
	pass

class DataTypeError(TypeError):
	pass

class DataSizeError(ValueError):
	pass


class Matrix:
	"""
	Matrice numérique réelle stockée en tableau 1D en format rangée-major.

	:param height: La hauteur (nb de rangées)
	:param width: La largeur (nb de colonnes)
	:param data: Si une liste, alors les données elles-mêmes (`data` affectée, pas copiée). Si un nombre, alors la valeur de remplissage
	"""

	def __init__(self, height, width, data = 0.0):
		if not isinstance(height, numbers.Integral) or not isinstance(width, numbers.Integral):
			raise DimensionsTypeError("Height and width of Matrix argument must be int")
		if height <= 0 or width <= 0:
			raise DimensionsError(f"height={height} and width={width} are not > 0")
		self.__height = height
		self.__width = width
		
		if isinstance(data, list):
			if len(data) != len(self):
				raise DataSizeError(f"Data length is {len(data)}, must be {len(self)}")
			self.__data = data
		elif isinstance(data, numbers.Number):
			self.__data = [data for _ in range(len(self))]
		else:
			raise DataTypeError("Data argument must be number or list")

	@property
	def height(self):
		return self.__height

	@property
	def width(self):
		return self.__width

	@property
	def data(self):
		return self.__data

	# TODO: Accès à un élément en lecture
	def TODO(TODO):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		self._check_indexes(indexes)
		# TODO: Retourner la valeur

	# TODO: Affectation à un élément
	def TODO(TODO):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		self._check_indexes(indexes)
		# TODO: L'affectation

	def __len__(self):
		"""
		Nombre total d'éléments
		"""
		return self.height * self.width

	# TODO: Représentation affichable (conversion pour print)
	def TODO(TODO):
		# TODO: Chaque rangée est sur une ligne, avec chaque élément séparé d'un espace.
		pass

	# TODO: Représentation officielle
	def TODO(TODO):
		# TODO: une string qui représente une expression pour construire l'objet.
		pass

	# TODO: String formatée
	def TODO(TODO):
		# TODO: On veut pouvoir dir comment chaque élément doit être formaté en passant la spécification de formatage qu'on passerait à `format()`
		pass

	def clone(self):
		return Matrix(self.height, self.width, self.data)

	def copy(self):
		return Matrix(self.height, self.width, copy.deepcopy(self.data))

	def has_same_dimensions(self, other):
		if not isinstance(other, Matrix):
			raise TypeError(type(other))
		return (self.height, self.width) == (other.height, other.width)
	
	def _check_indexes(self, indexes):
		if not isinstance(indexes, tuple) and len(indexes) == 2:
			raise IndexError(f"{indexes} is not tuple of two elements")
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError(f"{indexes} is not within (height={self.height}, width={self.width})")

	def __pos__(self):
		return self.copy()

	# TODO: Négation
	def TODO(TODO):
		pass

	# TODO: Addition
	def TODO(TODO):
		# TODO: D'abord vérifier que les opérandes ont les mêmes dimensions. Sinon, on lève un IncompatibleOperandsError.
		# TODO: Retourner le résultat de l'addition
		pass
	
	# TODO: Soustraction (n'oubliez pas qu'on a déjà l'opérateur de négation et d'addition)
	def TODO(TODO):
		pass
	
	# TODO: Multiplication matricielle/scalaire
	def TODO(TODO):
		if isinstance(other, Matrix):
			# TODO: D'abord vérifier que les opérandes on des dimensions compatibles. Sinon on lève un IncompatibleOperandsError.
			# TODO: Multiplication matricielle.
			# Rappel de l'algorithme simple pour C = A * B, où A, B sont matrices compatibles (hauteur_A = largeur_B)
			# C = Matrice(hauteur_A, largeur_B)
			# Pour i dans [0, hauteur_C[
				# Pour j dans [0, largeur_C[
					# Pour k dans [0, largeur_A[
						# C(i, j) = A(i, k) * B(k, j)
			pass
		elif isinstance(other, numbers.Number):
			# TODO: Multiplication scalaire.
			pass
		else:
			raise TypeError(type(other))

	# TODO: Multiplication scalaire avec le scalaire à gauche
	def TODO(TODO):
		pass

	def __abs__(self):
		return Matrix(self.height, self.width, [abs(e) for e in self.data])

	# TODO: Égalité entre deux matrices

	# TODO: Méthode de classe identity qui crée une matrice identité
	

