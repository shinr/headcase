class Color:
	r = 0.0
	g = 0.0
	b = 0.0
	a = 1.0
	def __init__(self, r, g, b, a):
		self.r, self.g, self.b, self.a = r, g, b, a

	def __eq__(self, other):
		if isinstance(other, Color):
			if other.r == self.r:
				if other.g == self.g:
					if other.b == self.b:
						if other.a == self.a:
							return True
			return False
		else:
			return NotImplemented

	def unwrap(self):
		return (self.r, self.g, self.b, self.a)
