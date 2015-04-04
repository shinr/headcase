from player import Player

class Level:
	entities = []
	player = None
	renderer = None
	def __init__(self, renderer):
		self.renderer = renderer
		self.player = Player()
		self.entities.append(self.player)

	def generate_level(self):
		pass

	def update(self, keys):
		for e in self.entities:
			e.update(keys)
		#self.player.update(keys)

	def render(self):
		for e in self.entities:
			self.renderer.queue(*e.render())
		self.renderer.render()