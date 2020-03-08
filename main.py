## We are using the module system
from rectangle import Rectangle as Rec
from triangle import Triangle as Tri
		
rec = Rec()
tri = Tri()

rec.set_values(12,10)
tri.set_values(3,10)

rec.set_color("blue")
tri.set_color("green")

print(rec.area())
print(tri.area())

print(rec.get_color())
print(tri.get_color())