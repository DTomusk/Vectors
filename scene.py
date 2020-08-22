import draw

# not sure this class is completely necessary
class Scene():
	def __init__(self, lines, circles, polygons):
		self.lines = lines
		self.circles = circles
		self.polygons = polygons

	def render(self, img, origin):
		for line in self.lines:
			draw.line(line, img, origin)
		for circle in self.circles:
			draw.circle(circle, img, origin)
		for poly in self.polygons:
			draw.polygon(poly, img, origin)

	def add_object(self, object):
		pass
