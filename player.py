from shaders.Shader import Shader
from OpenGL import GL
import sdl2
from vertex import Vertex
class Player:
	shader = None
	x = 0.0
	y = 0.0
	vertices = [Vertex(-.5, .5, 0.0),
				Vertex(.5, -.5, 0.0),
				Vertex(-.5, -.5, 0.0)]
	elements = [0, 1, 2]
	pos = None
	offset = 0
	def __init__(self):
		self.shader = Shader("player.vert", "player.frag")
		self.pos = GL.glGetUniformLocation(self.shader.program, "pos")

	def update(self, keys):
		if sdl2.SDLK_LEFT in keys:
			self.x -= 0.05
		if sdl2.SDLK_RIGHT in keys:
			self.x += 0.05
		if sdl2.SDLK_UP in keys:
			self.y += 0.05
		if sdl2.SDLK_DOWN in keys:
			self.y -= 0.05
		self.update_uniforms()

	def update_uniforms(self):
		# this works, but could it be done better?
		GL.glUseProgram(self.shader.program)
		GL.glUniform3f(self.pos, self.x, self.y, 0.0)

	def render(self):
		return (self.shader.program, len(self.elements), self.offset)

	def set_offset(self, offset):
		self.offset = offset
