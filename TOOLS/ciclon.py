# Descripcion


class Modular:

	''' Definir el objeto como Modular(numero, rango = (1,12) ) '''

	def __init__(self, num, rango = (1,12)):

		''' Definir el objeto como Modular(numero, rango = (1,12) ) '''

		if not isinstance(num, int):
			raise TypeError("La entrada debe ser del tipo int")
		elif not isinstance(rango, tuple):
			raise TypeError("El rango debe ser un tuple (max, min)")
#		elif not rango[0] <= num <= rango[1]:
#			raise TypeError("Entrada fuera de rango")

		self.__rango = rango
		self.__mod = rango[1] - rango[0] + 1
		self.__numero = self.__BuscarNumeroCongruencia(num)

#  |-----------------------------------------------------------------------------

	@classmethod
	def __Convertir(cls, num, rango):

		''' Regresar un obtjeto Modular desde la misma clase '''

		return cls(num, rango)

	@classmethod
	def __SumarRestar(cls, a, b, op):

		''' Reutiliza las funciones de suma para un uso más cómodo de
			la suma por la izquierda '''

		if op == "+":
			return a + b
		elif op == "-":
			return a - b

#  |-----------------------------------------------------------------------------

	def __repr__(self):

		''' Representación del objeto que se mostrará al usuario '''

		return '{} (mod {})'.format(self.__numero, self.__mod)

#  |-----------------------------------------------------------------------------

	def __add__(self, other):

		''' Sumar un par de elementos donde al menos uno es un objeto
			de la clase '''

		return self.__AddMin(other, "+")

	def __radd__(self, other):

		''' Sumar al objeto un elemento por la izquierda '''

		return Modular.__SumarRestar(self, other,  "+")

	def __sub__(self, other):

		''' Restar un par de elementos donde al menos uno es un objeto
			de la clase '''

		return self.__AddMin(other, "-")

	def __rsub__(self, other):

		''' Resta donde el objeto es el segundo elemento '''

		return Modular.__SumarRestar(self, other,  "-")

#  |-----------------------------------------------------------------------------

	def __int__(self):

		''' Regresa el valor de self.__numero cuando se aplica int() al objeto '''

		return self.__numero

#  |-----------------------------------------------------------------------------

	def __eq__(self, other):

		''' Comparación usando el operador == '''

		if type(other) == Modular:
			return self.__numero == other.__numero
		elif type(other) == int:
			return self.__numero == other
		else:
			return False

	def __ne__(self, other):

		''' Comparación usando el operador != '''

		if type(other) == Modular:
			return self.__numero != other.__numero
		elif type(other) == int:
			return self.__numero != other
		else:
			return False
#  |-----------------------------------------------------------------------------

	def __BuscarNumeroCongruencia(self, n):

		''' Encuentra el número entero positivo dentro del conjunto que sea
			de la misma clase de congruencia (modulo self.__mod) que la entrada n '''

		mini = self.__rango[0]
		maxi = self.__rango[1]

		while not mini <= n <= maxi:
			n = (n - mini) % self.__mod + mini

		return n
#  |-----------------------------------------------------------------------------

	def __AddMin(self, other, op):

		''' Auxiliar para calcular la suma y la resta del grupo '''

		if isinstance(other, int) or isinstance(other, float):
			if op == "+":
				return self.__numero + other
			elif op == "-":
				return self.__numero - other
		elif not isinstance(other, Modular):
			tipo = type(other)
			raise TypeError(f'La suma no se puede realizar con {tipo}')
		elif self.__rango != other.__rango:
			raise TypeError("Los objetos no tienen el mismo rango")

		if op == "+":
			self.r = self.__numero + other.__numero
		elif op == "-":
			self.r = self.__numero - other.__numero

		self.r = self.__BuscarNumeroCongruencia(self.r)

		return Modular.__Convertir(self.r, self.__rango)

#  |-----------------------------------------------------------------------------

	def crearMismoModulo(self, num):
		''' Crea otra instancia del objeto en el mismo rango '''

		return Modular.__Convertir(num, self.__rango)

	def getModulo(self):
		''' Obtiene el modulo del la instancia '''
		return self.__mod
