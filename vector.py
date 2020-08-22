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

	# scalar division
	def __truediv__(self, other):
		result = []
		for i in range(len(self)):
			result.append(self.data[i] / other)
		return Vector(result)

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

	# should round to a suitable degree just to avoid annoying problems 
	def __eq__(self, other):
		if len(self) != len(other):
			return False
		else:
			for i in range(len(self)):
				if round(self.data[i], 6) != round(other.data[i], 6):
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

	# Gives the unit vector with the same slope as the given vector 
	@staticmethod
	def unit(vector):
		return vector / vector.mod()

	# only for two dimensional, gives a vector with slope normal to the given vector  
	@staticmethod
	def normal(gradient_vector):
		return Vector([-1 * gradient_vector.data[1], gradient_vector.data[0]])

# could potentially be in any dimension (over 2), but we'll start with two 
class Line():
	def __init__(self, a, l):
		# a vector point that lies on the line 
		self.start = a
		# the slope of the line (also a vector), slope has size one to make some other things easier 
		self.slope = Vector.unit(l)

	# finds the point disp away from a that lies on the line (disp can be positive or negative)
	def coordinate(self, disp):
		return self.a + (disp * self.l)

	# find the intersection of two lines 
	def intersect(self, other):
		if (self.slope == other.slope) | (self.slope == -1 * other.slope):
			# not sure this should be an exception, do we expect inputs to intersect? 
			raise Exception("Given lines don't intersect")
		# need an else if to check whether they intersect an infinite amount of times 
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
			param = (by - ay + (ly / lx) * (ax - bx)) / ((ly * mx / lx) - my) 
			return other.start + (param * other.slope)

# not sure if I should include a vector to the center yet, or assume it's centered on the origin 
class Ellipse():
	def __init__(self, center, xradius, yradius):
		self.center = center
		self.x = xradius
		self.y = yradius

	# get the vector from the center to the edge with parameter t
	def vecAtT(self, t):
		return Vector([center[0] + self.x * math.cos(t), center[1] + self.y * math.sin(t)])

	def intersections(self, other):
		# two ellipses can intersect at zero, one, two, three, four, or infinite points 
		# one when they're just touching 
		# two when they overlap 
		# three when they overlap and part of one ellipse just touches the other 
		# four when they cross twice 
		# infinite when they're the exact same ellipse 
		pass

# circle are easier to work with than ellipses 
class Circle(Ellipse):
	def __init__(self, center, radius):
		self.center = center
		self.r = radius 

	def coordinate(self, t):
		return Vector([self.r * math.cos(t) + self.center.data[0], self.r * math.sin(t) + self.center.data[1]])

	def lineIntersection(self, line):
		radial_line = Line(self.center, Vector.normal(line.slope))
		line_intersect = radial_line.intersect(line)
		shortest_distance_to_line = (line_intersect - self.center).mod()
		if shortest_distance_to_line > self.r:
			# exception?
			raise Exception("No intersections")
		elif shortest_distance_to_line == self.r:
			return [line_intersect]
		# if the center of the circle lies on the line 
		elif shortest_distance_to_line == 0:
			intersection1 = self.center + self.r * (line.slope)
			intersection2 = self.center - self.r * (line.slope)
			return [intersection1, intersection2]
		else: 
			# get two intersects 
			pass