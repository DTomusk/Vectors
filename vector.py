import math

class Vector():
	def __init__(self, elements):
		self.data = elements

	def __len__(self):
		return len(self.data)

	# dot product
	def __mul__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		else:
			result = []
			for i in range(len(self)):
				result.append(self.data[i] * other.data[i])
			return sum(result)

	# cross product (might have to chose different operator)
	def __pow__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		elif len(self) == 3:
			i = (self.data[1] * other.data[2]) - (self.data[2] * other.data[1])
			j = (self.data[2] * other.data[0]) - (self.data[0] * other.data[2])
			k = (self.data[0] * other.data[1]) - (self.data[1] * other.data[0])
			return Vector([i, j, k])
		else:
			pass

	# multiplying a scalar and a vector 
	def __rmul__(self, other):
		result = []
		for i in range(len(self)):
			result.append(self.data[i] * other)
		return Vector(result)

	def __add__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		else:
			result = []
			for i in range(len(self)):
				result.append(self.data[i] + other.data[i])
			return Vector(result)

	def __sub__(self, other):
		if len(self) != len(other):
			raise Exception("Vectors must be of the same dimension")
		else:
			return self + (-1 * other)

	def __str__(self):
		string = "("
		for i in range(len(self) - 1):
			string += str(self.data[i]) + ", "
		string += str(self.data[len(self)-1]) + ")"
		return string

	def __eq__(self, other):
		if len(self) != len(other):
			return False
		else:
			for i in range(len(self)):
				if self.data[i] != other.data[i]:
					return False
			return True

	def mod(self):
		result = 0
		for i in range(len(self)):
			result += self.data[i]**2
		return math.sqrt(result)

	def angle(self, other):
		if self.mod() == 0 | other.mod() == 0:
			raise Exception("Vectors must have non zero length to find angle subtended")
		else:
			return math.acos((self * other) / (self.mod() * other.mod()))

# could potentially be in any dimension (over 2), but we'll start with two 
class Line():
	def __init__(self, a, l):
		# a vector point that lies on the line 
		self.start = a
		# the slope of the line (also a vector)
		self.slope = l

	# finds the point disp away from a that lies on the line (disp can be positive or negative)
	def coordinate(self, disp):
		return self.a + (disp * self.l)

	# find the intersection of two lines 
	def intersect(self, other):
		if self.slope == other.slope | self.slope == -1 * other.slope:
			# not sure this should be an exception, do we expect inputs to intersect? 
			raise Exception("Given lines don't intersect")
		else:
			# mainly for readability
			ax = self.start.data[0]
			ay = self.start.data[1]
			bx = other.start.data[0]
			by = other.start.data[1]
			lx = self.slope.data[0]
			ly = self.slope.data[1]
			mx = other.slope.data[0]
			my = other.slope.data[1]
			param = (by - ay + (ly / lx) * (ax - bx)) / (mx - my) 
			return other.start + (param * other.slope)