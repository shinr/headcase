from shaders.Shader import Shader
from pyglet import gl
from pyglet.window import key

class Player:
	shader = None
	rect = [-1.0, -1.0, 1.0, 1.0]
	x = 0.0
	y = 0.0
	vertices = [1.0, 1.0, 0.0,
				-1.0, 1.0, 0.0,
				-1.0, -1.0, 0.0]
	def __init__(self):
		self.shader = Shader("player.vert", "player.frag")

	def render(self):
		pass

	def update(self, keys):
		if key.LEFT in keys:
			self.x -= 0.1
		if key.RIGHT in keys:
			self.x += 0.1
		if key.UP in keys:
			self.y += 0.1
		if key.DOWN in keys:
			self.y -= 0.1
