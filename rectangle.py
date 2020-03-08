from polygon import Polygon
from shape import Shape

# one class can inhiret from multiple classes

class Rectangle(Polygon, Shape):
	
	def area(self):
		return self.get_height() * self.get_width()