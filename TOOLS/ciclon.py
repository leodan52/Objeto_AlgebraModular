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

		self.rango = rango
		self.mod = rango[1] - rango[0] + 1
		self.n = self.RelCongr(num)

#  |-----------------------------------------------------------------------------

	@classmethod
	def convertir(cls, num, rango):

		''' Regresar un obtjeto Modular desde la misma clase '''

		return cls(num, rango)

	@classmethod
	def SumaResta(cls, a, b, op):

		''' Reutiliza las funciones de suma para un uso más cómodo de
			la suma por la izquierda '''

		if op == "+":
			return a + b
		elif op == "-":
			return a - b

#  |-----------------------------------------------------------------------------

	def __repr__(self):

		''' Representación del objeto que se mostrará al usuario '''

		return '{} (mod {})'.format(self.n, self.mod)

#  |-----------------------------------------------------------------------------

	def __add__(self, other):

		''' Sumar un par de elementos donde al menos uno es un objeto
			de la clase '''

		return self.AddMin(other, "+")

	def __radd__(self, other):

		''' Sumar al objeto un elemento por la izquierda '''

		return Modular.SumaResta(self, other,  "+")

	def __sub__(self, other):

		''' Restar un par de elementos donde al menos uno es un objeto
			de la clase '''

		return self.AddMin(other, "-")

	def __rsub__(self, other):

		''' Resta donde el objeto es el segundo elemento '''

		return Modular.SumaResta(self, other,  "-")

#  |-----------------------------------------------------------------------------

	def __int__(self):

		''' Regresa el valor de self.n cuando se aplica int() al objeto '''

		return self.n

#  |-----------------------------------------------------------------------------

	def __eq__(self, other):

		''' Comparación usando el operador == '''

		if type(other) == Modular:
			return self.n == other.n
		elif type(other) == int:
			return self.n == other
		else:
			return False

	def __ne__(self, other):

		''' Comparación usando el operador != '''

		if type(other) == Modular:
			return self.n != other.n
		elif type(other) == int:
			return self.n != other
		else:
			return False
#  |-----------------------------------------------------------------------------

	def RelCongr(self, n):

		''' Encuentra el número entero positivo dentro del conjunto que sea
			de la misma clase de congruencia (modulo self.mod) que la entrada n '''

		mini = self.rango[0]
		maxi = self.rango[1]

		while not mini <= n <= maxi:
			n = (n - mini) % self.mod + mini

		return n
#  |-----------------------------------------------------------------------------

	def AddMin(self, other, op):

		''' Auxiliar para calcular la suma y la resta del grupo '''

		if isinstance(other, int) or isinstance(other, float):
			if op == "+":
				return self.n + other
			elif op == "-":
				return self.n - other
		elif not isinstance(other, Modular):
			tipo = type(other)
			raise TypeError(f'La suma no se puede realizar con {tipo}')
		elif self.rango != other.rango:
			raise TypeError("Los objetos no tienen el mismo rango")

		if op == "+":
			self.r = self.n + other.n
		elif op == "-":
			self.r = self.n - other.n

		self.r = self.RelCongr(self.r)

		return Modular.convertir(self.r, self.rango)
