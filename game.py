import pyglet
from pyglet import gl, event
from player import Player
from renderer import Renderer
import ctypes

class Game(pyglet.window.Window):
	entities = []
	keys = []
	renderer = None
	def __init__(self, width, height):
		super(Game, self).__init__(width, height)
		self.entities.append(Player())

	def on_draw(self):
		self.renderer.render()
		

		# draw ....
		

	# initialize gl
	def on_resize(self, width, height):
		print ctypes.string_at(gl.glGetString(gl.GL_VERSION))
		print ctypes.string_at(gl.glGetString(gl.GL_SHADING_LANGUAGE_VERSION))
		print "-------"
		self.renderer = Renderer()
		self.renderer.queue(*self.entities)
		gl.glEnable(gl.GL_DEPTH_TEST)
		gl.glEnable(gl.GL_BLEND)
		gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
		gl.glEnable(gl.GL_CULL_FACE)
		gl.glCullFace(gl.GL_BACK);
		gl.glClearColor(0.2, 0.2, 0.2, 1.0)
		gl.glViewport(0, 0, width, height)
		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		gl.gluPerspective(65, width / float(height), .1, 1000)
		gl.glMatrixMode(gl.GL_MODELVIEW)

		return event.EVENT_HANDLED

	def update(self, dt):
		self.entities[0].update(self.keys)

	def on_key_press(self, button, modifiers):
		if not button in self.keys: 
			self.keys.append(button)

	def on_key_release(self, button, modifiers):
		if button in self.keys: 
			self.keys.remove(button)

	

if __name__ == '__main__':
	gl.glfwWindowHint(gl.GLFW_CONTEXT_VERSION_MAJOR, 3);
	gl.glfwWindowHint(gl.GLFW_CONTEXT_VERSION_MINOR, 3);
	gl.glfwWindowHint(gl.GLFW_OPENGL_PROFILE, gl.GLFW_OPENGL_CORE_PROFILE);
	gl.glfwWindowHint(gl.GLFW_OPENGL_FORWARD_COMPAT, gl.GL_TRUE);

	game = Game(800, 600)
	pyglet.clock.schedule_interval(game.update, 1/120.0)
	pyglet.app.run()