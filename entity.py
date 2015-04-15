from shaders.Shader import Shader
from OpenGL import GL
import sdl2
from vertex import Vertex
from PIL import Image
import resources
import random
class Entity:
	shader = None
	x = 0.0
	y = 0.0
	vertices = None
	texture = 0
	texture_image = None
	elements = None
	offset = 0
	def __init__(self, x, y, vert, frag, texture_name=None):
		self.x, self.y = x, y
		self.shader = Shader(vert, frag)
		self.vertices = [
		Vertex(x + 0.3, y - 0.3, 0.0), 
		Vertex(x + 0.3, y + 0.3, 0.0), 
		Vertex(x - 0.3, y - 0.3, 0.0), 
		Vertex(x - 0.3, y + 0.3, 0.0), 
		Vertex(x, y - 0.5, 0.0),  
		Vertex(x, y + 0.5, 0.0)] 
		self.elements = [3, 1, 5, 2, 0, 4, 3, 1, 0, 3, 0, 2]
		if texture_name:
			self.texture_image = Image.open(resources.get_file(texture_name))

	def update(self, dt):
		self.update_uniforms()

	def update_uniforms(self):
		pass

	def render(self):
		return (self.shader.program, self.texture, len(self.elements), self.offset)

	def set_offset(self, offset):
		self.offset = offset

