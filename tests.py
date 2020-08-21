import unittest 
from vector import Vector

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

	#def test_scalar_multiplication(self):

if __name__ == '__main__':
	unittest.main()