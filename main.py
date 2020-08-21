from vector import Vector, Line

def main():
	vec1 = Vector([1, 2, 3])
	vec2 = Vector([1, 0, 1])
	print(vec1)
	print(vec2)
	print(vec1 + vec2)
	print(3 * vec1)
	print(vec1 * vec2)
	print(vec1 ** vec2)

if __name__=="__main__":
	main()