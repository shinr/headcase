from player import Player

class Level:
	entities = []
	player = None
	renderer = None
	def __init__(self, renderer):
		self.renderer = renderer
		self.player = Player()

	def generate_level(self):
		pass

	def update(self, keys):
		for e in self.entities:
			e.update()
		self.player.update(keys)

	def render(self):
		self.renderer.render(self.player.shader.program)