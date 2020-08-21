import math

class Vector():
	def __init__(self, elements):
		self.data = elememts

	def __len__(self):
		return len(self.data)

	# dot product
	def __mul__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		else:
			result = []
			for i in range(len(self)):
				result.append(self[i] * other[i])
			return Vector(result)

	# cross product (might have to chose different operator)
	def __pow__(self, other):
		pass

	# multiplying a scalar and a vector 
	def __rmul__(self, other):
		for x in self.data:
			x *= other 
		return self

	def __add__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		else:
			result = []
			for i in range(len(self)):
				result.append(self[i] + other[i])
			return Vector(result)

	def __sub__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		else:
			return self + (-1 * other)

	def __str__(self):
		string = "("
		for i in range(len(self)):
			string += str(self.data[i]) + ", "
		string += ")"
		return string

	def mod(self):
		result = 0
		for i in range(len(self)):
			result += self.data[i]**2
		return math.sqrt(result)