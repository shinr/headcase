class Vertex:
	x = 0.0
	y = 0.0
	z = 0.0
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	def __eq__(self, vertex):
		if isinstance(vertex, Vertex):
			if vertex.x == self.x:
				if vertex.y == self.y:
					if vertex.z == self.z:
						return True
			return False
		else:
			return NotImplemented

	def unwrap(self):
		return self.x, self.y, self.z


