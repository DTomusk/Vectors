import math 
from vector import Vector, Line, Circle, Arc
# test case for drawing program and also for personal interest 
# draw patterns in a hyperbolic plane 

# get the arc formed by the intersections of the circle and radial lines at the given angles 
def arc_from_angles(circle, first, second):
	# pretty much the same calculation four times, could be put somewhere else 
	x1 = circle.center.data[0] + circle.r * math.cos(first)
	y1 = circle.center.data[1] + circle.r * math.sin(first)
	x2 = circle.center.data[0] + circle.r * math.cos(second)
	y2 = circle.center.data[1] + circle.r * math.sin(first)
	return arc_from_points(circle, Vector([x1, y1]), Vector([x2, y2]))

# given a circle and two points lying on it find the arc between those points 
def arc_from_points(circle, first, second):
	my_focus = focus(circle, first, second)
	arc_radius = (my_focus - first).mod()
	# the two angles that describe this arc are given by the slopes of the normals
	# the slope of a normal gives two angles 
	# we can use the dot product to find the angle between the vector 1,0 and focus - first or second
	right_vector = Vector([1,0])
	angle1 = (my_focus - first).angle(right_vector)
	angle2 = (my_focus - second).angle(right_vector)
	return Arc(my_focus, arc_radius, angle1, angle2)

def focus(circle, first, second):
	# the gradient of the tangent is normal to the gradient between the point and the center
	tangent1 = Vector.normal(Vector.gradient(first, circle.center))
	tangent2 = Vector.normal(Vector.gradient(second, circle.center))

	# the lines start at the points given and have a slope given by the tangents 
	line1 = Line(Vector(first), tangent1)
	line2 = Line(Vector(second), tangent2)

	return line1.intersect(line2)