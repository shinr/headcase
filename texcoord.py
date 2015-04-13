class TexCoord:
	x = 0.0
	y = 0.0
	def __init__(self, x, y):
		self.x, self.y = x, y

	def __eq__(self, other):
		if isinstance(other, TexCoord):
			if other.x == self.x:
				if other.y == self.y:
					return True
			return False
		else:
			return NotImplemented

	def unwrap(self):
		return (self.x, self.y)
