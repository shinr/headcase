from player import Player
from entity import Entity
class Level:
	entities = []
	player = None
	renderer = None
	def __init__(self, renderer):
		self.renderer = renderer
		self.player = Player()
		self.entities.append(self.player)
		self.generate_level()

	def generate_level(self):
		self.entities.append(Entity("static.vert", "player.frag"))
		for e in self.entities:
			self.renderer.queue_data(e.vertices, e.elements, e)
		self.renderer.load_vertex_data(self.renderer.vertices, self.renderer.elements, True)

	def update(self, keys):
		for e in self.entities:
			e.update(keys)
		#self.player.update(keys)

	def render(self):
		for e in self.entities:
			self.renderer.queue(*e.render())
		self.renderer.render()