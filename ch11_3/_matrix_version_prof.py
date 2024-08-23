"""
Chapitre 11.2
"""


from multiprocessing import Value
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
	def __getitem__(self, indexes):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		self._check_indexes(indexes)
		# TODO: Retourner la valeur
		return self.data[indexes[0] * self.width + indexes[1]]

	# TODO: Affectation à un élément
	def __setitem__(self, indexes, value):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		self._check_indexes(indexes)
		# TODO: L'affectation
		self.data[indexes[0] * self.width + indexes[1]] = value

	def __len__(self):
		"""
		Nombre total d'éléments
		"""
		return self.height * self.width

	# TODO: Représentation affichable (conversion pour print)
	def __str__(self):
		# TODO: Chaque rangée est sur une ligne, avec chaque élément séparé d'un espace.
		return format(self, "") # On réutilise notre __format__ avec une spec vide pour éviter de se répéter.

	# TODO: Représentation officielle
	def __repr__(self):
		# TODO: une string qui représente une expression pour construire l'objet.
		return f"Matrix({self.height}, {self.width}, {repr(self.data)})"

	# TODO: String formatée
	def __format__(self, format_spec):
		# TODO: On veut pouvoir dir comment chaque élément doit être formaté en passant la spécification de formatage qu'on passerait à `format()`
		lines = []
		for i in range(self.height):
			line = " ".join([format(self[i, j], format_spec) for j in range(self.width)])
			lines.append(line)
		return "\n".join(lines)

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
	def __neg__(self):
		return Matrix(self.height, self.width, [-e for e in self.data])

	# TODO: Addition
	def __add__(self, other):
		# TODO: D'abord vérifier que les opérandes ont les mêmes dimensions. Sinon, on lève un IncompatibleOperandsError.
		if not self.has_same_dimensions(other):
			raise IncompatibleOperandsError(f"{other.height}, {other.width}")
		# TODO: Retourner le résultat de l'addition
		return Matrix(self.height, self.width, [e1 + e2 for e1, e2 in zip(self.data, other.data)])
		# Autre façon de faire :
		#result = Matrix(self.height, self.width)
		#for i in range(len(self)):
		#	result.data[i] = self.data[i] + other.data[i]
		#return result
	
	# TODO: Soustraction (n'oubliez pas qu'on a déjà l'opérateur de négation et d'addition)
	def __sub__(self, other):
		return self + -other
	
	# TODO: Multiplication matricielle/scalaire
	def __mul__(self, other):
		if isinstance(other, Matrix):
			# TODO: Multiplication matricielle.

			# TODO: Vérifier compatibilité.
			if self.width != other.height:
				raise IncompatibleOperandsError(f"{other.height}, {other.width}")

			# Rappel de l'algorithme simple pour C = A * B, où A, B sont matrices compatibles (largeur_A = hauteur_B)
			# C = Matrice(hauteur_A, largeur_B)
			result = Matrix(self.height, other.width)
			# Pour i dans [0, hauteur_C[
			for i in range(result.height):
				# Pour j dans [0, largeur_C[
				for j in range(result.width):
					# Pour k dans [0, hauteur_B[
					for k in range(other.height):
						# C(i, j) += A(i, k) * B(k, j)
						result[i, j] += self[i, k] * other[k, j]
			return result
		elif isinstance(other, numbers.Number):
			# TODO: Multiplication scalaire.
			return Matrix(self.height, self.width, [e * other for e in self.data])
		else:
			raise TypeError(type(other))

	# TODO: Multiplication scalaire avec le scalaire à gauche
	def __rmul__(self, other):
		return self * other

	def __abs__(self):
		return Matrix(self.height, self.width, [abs(e) for e in self.data])

	# TODO: Égalité entre deux matrices
	def __eq__(self, other):
		return self is other or (self.height, self.width, self.data) == (other.height, other.width, other.data)

	# Définit implicitement par l'interpréteur
	#def __ne__(self, other):
	#	return not self == other

	@classmethod
	def identity(cls, width):
		result = cls(width, width)
		for i in range(width):
			result[i, i] = 1.0
		return result

