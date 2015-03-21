from shaders.Shader import Shader
from OpenGL import GL
import sdl2
class Player:
	shader = None
	rect = [-1.0, -1.0, 1.0, 1.0]
	x = 0.0
	y = 0.0
	vertices = [1.0, 1.0, 0.0,
				-1.0, 1.0, 0.0,
				-1.0, -1.0, 0.0]
	pos = None
	def __init__(self):
		self.shader = Shader("player.vert", "player.frag")
		self.pos = GL.glGetUniformLocation(self.shader.program, "pos")
		print self.pos

	def render(self):
		pass

	def update(self, keys):
		if sdl2.SDLK_LEFT in keys:
			self.x -= 0.1
		if sdl2.SDLK_RIGHT in keys:
			self.x += 0.1
		if sdl2.SDLK_UP in keys:
			self.y += 0.1
		if sdl2.SDLK_DOWN in keys:
			self.y -= 0.1
		GL.glUniform3f(self.pos, self.x, self.y, 0.0)
