from shaders.Shader import Shader
from OpenGL import GL
import sdl2
from vertex import Vertex
class Entity:
	shader = None
	x = 0.0
	y = 0.0
	vertices = [Vertex(0.3, -.3, 0.0),
				Vertex(-0.3, -.3, 0.0),
				Vertex(-0.3, 0.3, 0.0),
				Vertex(0.3, 0.6, 0.0),
				Vertex(0.3, -.6, 0.0),
				Vertex(0.3, 0.3, 0.0)]
	elements = [0, 1, 2, 0, 3, 2, 0, 4, 5, 0, 3, 5]
	offset = 0
	def __init__(self, vert, frag, texture):
		self.shader = Shader(vert, frag)

	def update(self, dt):
		self.update_uniforms()

	def update_uniforms(self):
		pass

	def render(self):
		return (self.shader.program, len(self.elements), self.offset)

	def set_offset(self, offset):
		self.offset = offset