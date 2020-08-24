from vector import Vector, Line, Circle
from PIL import Image, ImageOps
import draw
import math
import hyper

IMG_DIM = (1200, 800)
ORIGIN = (IMG_DIM[0] / 2, IMG_DIM[1] / 2)
SCALE = 100

def main():
	img = Image.new('RGB', IMG_DIM, color = 'white')

	my_circle = Circle(Vector([200,50]), 100)
	circle_2 = Circle(Vector([0,0]), 300)

	arc = hyper.arc_from_angles(my_circle, math.pi / 3, 3 * math.pi / 4)

	draw.axes(img, ORIGIN)

	draw.circle(my_circle, img, ORIGIN)

	draw.circle_segment(circle_2, math.pi / 2, 5 * math.pi / 4, img, ORIGIN)

	draw.line((0,0), (200,300), img, ORIGIN)

	draw.circle_segment(arc, img, ORIGIN)

	img = ImageOps.flip(img)

	img.save('new.png')
	

if __name__=="__main__":
	main()