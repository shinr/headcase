from shaders.Shader import Shader
from OpenGL import GL
import sdl2
from vertex import Vertex
from PIL import Image
from entity import Entity
class Player(Entity):
	pos = None
	layer = 5
	def __init__(self):
		super(Player, self).__init__(0.0, 0.0, 'player.vert', 'player.frag')
		self.pos = GL.glGetUniformLocation(self.shader.program, "pos")
		self.elements = [0, 1, 2]
		self.vertices = [Vertex(-.5, .5, 0.0),
				Vertex(.5, -.5, 0.0),
				Vertex(-.5, -.5, 0.0)]
		self.layer = 5
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