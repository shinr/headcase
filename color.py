class Color:
	r = 0.0
	g = 0.0
	b = 0.0
	a = 1.0
	def __init__(self, r, g, b, a):
		self.r, self.g, self.b, self.a = r, g, b, a

	def __eq__(self, other):
		pass

	def unwrap(self):
		return (self.r, self.g, self.b, self.a)

c = Color(1.0, 1.0, 1.0, 1.0)
print c, c.unwrap()