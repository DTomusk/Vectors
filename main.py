from vector import Vector, Line, Circle
from PIL import Image, ImageOps
import draw

IMG_DIM = (1200, 800)
ORIGIN = (IMG_DIM[0] / 2, IMG_DIM[1] / 2)
SCALE = 100

# a scene object contains all the objects to be drawn 
def render(scene):
	pass

def main():
	img = Image.new('RGB', IMG_DIM, color = 'white')

	my_circle = Circle(Vector([200,50]), 100)

	draw.circle(my_circle, img, ORIGIN)

	draw.line((0,0), (200,300), img, ORIGIN)

	img = ImageOps.flip(img)

	img.save('new.png')
	

if __name__=="__main__":
	main()