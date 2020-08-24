from vector import Vector, Line, Circle
import math

def circle(circle, img, origin):
	# number of pixels depends on size of circle (earlier had flat number)
	circumference = math.pi * circle.r**2
	for t in range(int(circumference)):
		angle = 2 * t * math.pi / circumference
		point = adjust(circle.coordinate(angle), origin)
		img.putpixel(point, (0,0,0))

# similar to circle but limited to between two angles 
# angle in radians 
def circle_segment(arc, img, origin):
	angle_spanned = abs(arc.angle1 - arc.angle2)
	circumference = math.pi * arc.r**2
	arc_length = circumference * (angle_spanned / (2 * math.pi))
	for t in range(int(arc_length)):
		angle = start_angle + (2 * t * math.pi / circumference)
		point = adjust(arc.coordinate(angle), origin)
		img.putpixel(point, (0,0,0))

# line needs to be equally pixel dense regardless of slope, not sure how 
# get length of line, for a certain unit of length draw a certain number of pixels 
# the length calculation ideally wouldn't be in this file 
# could use separate functions for drawing lines of a known length and lines of a known start and end 
def line(start, end, img, origin):
	length = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
	slope = Vector.unit(Vector([end[0] - start[0], end[1] - start[1]]))
	line = Line(Vector(start), slope)
	line_of_length(line, length, img, origin)

def line_of_length(line, length, img, origin):
	for t in range(2 * int(length)):
		point = adjust(line.start + t * line.slope / 2, origin)
		img.putpixel(point, (0,0,0))

def axes(img, origin):
	for x in range(img.size[0]):
		img.putpixel((x, int(origin[1])), (0,0,0))
	for y in range(img.size[1]):
		img.putpixel((int(origin[0]), y), (0,0,0))

# takes a vector and shoots out a pixel coordinate 
def adjust(point, origin):
	return (int(point.data[0] + origin[0]), int(point.data[1] + origin[1]))
