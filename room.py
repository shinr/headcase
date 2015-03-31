from shaders.Shader import Shader
from OpenGL import GL
# container class

class Room:
	exits = []
	vertices  = []
	elements = []
	shader = None
	def __init__(self, vertices, frag, vert):
		self.vertices = vertices
		self.shader = Shader(vert, frag)

	def link(self, *rooms):
		self.exits.extend(rooms)

	def render(self):
		return (self.shader, self.elements)

