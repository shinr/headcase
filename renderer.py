from pyglet import gl

class Renderer:
	queue = {}

	def __init__(self):
		pass

	def queue(self, *objects):
		pass

	def render(self):
		for shader, object_list in self.queue:
			gl.glUseProgram(shader)
			