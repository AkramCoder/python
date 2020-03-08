class Car:
	def __init__(self, speed, color, *args, **kwargs):
		self.color = color
		# private atribute
		self.__speed = speed

	

	# getters- setters
	def get_speed(self):
		return self.__speed
	def set_speed(self, value):
		self.__speed = value

	def speed_color(self):
		print(self.__speed_color())

	# private method can be used only inside the class
	def __speed_color(self):
		return "{}, {}".format(self.color,self.get_speed())



ford = Car(12,"gg")
audi = Car(134,"YFF")

# this line has no meanning
ford.__speed = 123

ford



#print(ford.name)