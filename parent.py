class Parent:
	
	def __init__(self, fname):
		self.fname = fname

class Parent1:
	
	def __init__(self,lname):
		self.lname = lname

class Child(Parent):
	def __init__(self, age):
		
		self.age = age

	def info(self):
		return "{}".format(self.age)


		

c = Child(12)
print(c.info())
		

