from shaders.Shader import Shader
from pyglet import gl
from pyglet.window import key

class Player:
	shader = None
	rect = [-1.0, -1.0, 1.0, 1.0]
	x = 0.0
	y = 0.0
	vertices = []
	def __init__(self):
		self.shader = Shader("player.vert", "player.frag")

	def render(self):
		gl.glUseProgram(self.shader.program)
		#gl.glUniform1f(self.shader.uniform_location)
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(self.x + self.rect[0], self.y + self.rect[3], 0.0)
		gl.glVertex3f(self.x + self.rect[0], self.y + self.rect[1], 0.0)
		gl.glVertex3f(self.x + self.rect[2], self.y + self.rect[1], 0.0)
		gl.glVertex3f(self.x + self.rect[2], self.y + self.rect[3], 0.0)
		gl.glEnd()

	def update(self, keys):
		if key.LEFT in keys:
			self.x -= 0.1
		if key.RIGHT in keys:
			self.x += 0.1
		if key.UP in keys:
			self.y += 0.1
		if key.DOWN in keys:
			self.y -= 0.1
