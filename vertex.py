from color import Color
from texcoord import TexCoord
import random 

class Vertex:
	x = 0.0
	y = 0.0
	z = 0.0
	w = 1.0
	color = None
	texcoord = None
	def __init__(self, x, y, z, r=None, g=None, b=None, a=None, tx=0.0, ty=0.0):
		if not r or not b or not g or not a:
			r, g, b, a = random.random(),random.random(),random.random(),1.0
		self.x, self.y, self.z = x, y, z
		self.color = Color(r, g, b, a)
		self.texcoord = TexCoord(tx, ty)
	def __eq__(self, vertex):
		if isinstance(vertex, Vertex):
			if vertex.x == self.x:
				if vertex.y == self.y:
					if vertex.z == self.z:
						if self.color == vertex.color:
							return True
			return False
		else:
			return NotImplemented

	def randomize(self, x=0.0, y=0.0):
		self.x = x -random.random() + random.random()
		self.y = y -random.random() + random.random()
		self.z = -random.random() + random.random()
		return self

	def unwrap(self):
		r, g, b, a = self.color.unwrap()
		return self.x, self.y, self.z, self.w, r, g, b, a


