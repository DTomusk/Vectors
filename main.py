from vector import Vector, Line, Circle
from PIL import Image
import draw

IMG_DIM = (1200, 800)
ORIGIN = (IMG_DIM[0] / 2, IMG_DIM[1] / 2)
SCALE = 100

def main():
	img = Image.new('RGB', IMG_DIM, color = 'white')

	my_circle = Circle(Vector([0,0]), 100)

	draw.circle(img, my_circle, ORIGIN)

	img.save('new.png')
	

if __name__=="__main__":
	main()