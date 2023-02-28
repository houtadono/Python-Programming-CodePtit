
class Rectangle:
	def __init__(self,a,b,c):
		self.x = a
		self.y = b
		self.c = c

	def perimeter(self):
		return (self.x+self.y)*2
	def area(self):
		return self.x*self.y
	def color(self):
		return c.title()
		


a,b,c = input().split()
r = Rectangle(int(a),int(b),c)
if r.x>0 and r.y>0: 
	print(r.perimeter(),r.area(),r.color())
else: print("INVALID")

# done