from shaders.Shader import Shader
from pyglet import gl
from pyglet.window import key

class Player:
	shader = None
	x = 0.0
	y = 0.0
	def __init__(self):
		self.shader = Shader("player.vert", "player.frag")

	def render(self):
		hd = 1.0
		
		gl.glUseProgram(self.shader.program)
		gl.glUniform1f(shader.uniform_location)
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(self.x - hd, self.y + hd,hd)
		gl.glVertex3f(self.x - hd, self.y - hd,hd)
		gl.glVertex3f(self.x + hd, self.y - hd,hd)
		gl.glVertex3f(self.x + hd, self.y + hd,hd)
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
