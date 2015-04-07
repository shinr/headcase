from entity import Entity

class Box(Entity):
	def __init__(self, vert, frag, x, y):
		super(Box, self).__init__(vert, frag)
		