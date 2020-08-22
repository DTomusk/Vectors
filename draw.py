from vector import Vector, Line, Circle
import math

def circle(img, circle, origin):
	for t in range(1024):
		angle = t * math.pi / 512
		point = adjust(circle.coordinate(angle), origin)
		img.putpixel(point, (0,0,0))

# takes a vector and shoots out a pixel coordinate 
def adjust(point, origin):
	return (int(point.data[0] + origin[0]), int(point.data[1] + origin[1]))
