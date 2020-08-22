import unittest 
import math
from vector import Vector, Line, Circle

class TestVectorMethods(unittest.TestCase):
	def test_addition(self):
		vec1 = Vector([1,2,3])
		vec2 = Vector([2,-1,1])
		vec3 = Vector([3,3,-2])
		self.assertEqual(vec1 + vec2, Vector([3,1,4]))
		self.assertEqual(vec1 + vec3, Vector([4,5,1]))

	def test_dot_product(self):
		vec1 = Vector([1,2,3])
		vec2 = Vector([2,-1,1])
		vec3 = Vector([3,3,-2])
		self.assertEqual(vec1 * vec2, 3)

	def test_cross_product(self):
		vec1 = Vector([1,2,3])
		vec2 = Vector([2,-1,1])
		vec3 = Vector([3,3,-2])
		self.assertEqual(vec1 ** vec1, Vector([0,0,0]))
		self.assertEqual(vec2 ** vec3, Vector([-1,7,9]))

	def test_unit_vector(self):
		vec1 = Vector([1,2,3])
		vec2 = Vector([2,-1,1])
		root14 = math.sqrt(14)
		root6 = math.sqrt(6)

		self.assertEqual(Vector.unit(vec1), Vector([1 / root14, 2 / root14, 3 / root14]))
		self.assertEqual(Vector.unit(vec2), Vector([2 / root6, -1 / root6, 1 / root6]))

	def test_line_intersect(self):
		line1 = Line(Vector([0,0]), Vector([1,1]))
		line2 = Line(Vector([0,5]), Vector([1,2]))
		line3 = Line(Vector([0,-2]), Vector([4,1]))

		self.assertEqual(line1.intersect(line2), Vector([-5,-5]))
		self.assertEqual(line2.intersect(line3), Vector([-4,-3]))

	def test_circle_line_intersect(self):
		circle = Circle(Vector([0,0]), 1)
		line1 = Line(Vector([0,0]), Vector([1,1]))
		line2 = Line(Vector([-math.sqrt(2) / 2, math.sqrt(2) / 2]), Vector([1,1]))

		intersects1 = circle.lineIntersection(line1)
		intersects2 = circle.lineIntersection(line2)

		self.assertEqual(len(intersects1), 2)
		self.assertEqual(len(intersects2), 1)

		self.assertEqual(intersects1, [Vector([1 / math.sqrt(2), 1 / math.sqrt(2)]), Vector([-1 / math.sqrt(2), -1 / math.sqrt(2)])])
		self.assertEqual(intersects2[0], Vector([-1 / math.sqrt(2), 1 / math.sqrt(2)]))

	#def test_scalar_multiplication(self):

if __name__ == '__main__':
	unittest.main()