from OpenGL import GL
from player import Player
from renderer import Renderer
import ctypes
#import cyglfw3 as glfw
import sdl2
from sdl2 import video

from shaders.Shader import Shader

class Game:
	entities = []
	keys = []
	renderer = None
	window = None
	context = None
	def __init__(self, width, height):
		if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
			print (sdl2.SDL_GetError())
			return -1
		self.window = sdl2.SDL_CreateWindow(b"Headcase", 
												sdl2.SDL_WINDOWPOS_UNDEFINED,
												sdl2.SDL_WINDOWPOS_UNDEFINED,
												width,
												height,
												sdl2.SDL_WINDOW_OPENGL)
		if not self.window:
			print(sdl2.SDL_GetError())
			return -1
		video.SDL_GL_SetAttribute(video.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
		video.SDL_GL_SetAttribute(video.SDL_GL_CONTEXT_MINOR_VERSION, 2)
		video.SDL_GL_SetAttribute(video.SDL_GL_CONTEXT_PROFILE_MASK,
		video.SDL_GL_CONTEXT_PROFILE_CORE)
		self.context = sdl2.SDL_GL_CreateContext(self.window)
		print ctypes.string_at(GL.glGetString(GL.GL_VERSION))
		print ctypes.string_at(GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION))
		print "setting up renderer"
		print "--------------------------"
		self.renderer = Renderer()
		print "setting up shaders"
		print "--------------------------"
		self.entities.append(Player())
		self.renderer.shader = Shader("static.vert", "player.frag")
		self.renderer.program = self.entities[0].shader.program
		self.renderer.setup_vao()
		

	def on_draw(self):		
		self.renderer.render()
		

		# draw ....

	def update(self):
		self.entities[0].update(self.keys)

	# maybe a better way would be to map keys to actions and then do those actions on keypress
	def input_key_pressed(self, key, repeat):
		if repeat > 0:
			return
		if key not in self.keys:
			self.keys.append(key)

	def input_key_released(self, key, repeat):
		if repeat > 0:
			return
		if key in self.keys:
			self.keys.remove(key)

	def loop(self):
		print "ready"
		event = sdl2.SDL_Event()
		running = True
		while running:
			while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
				if event.type == sdl2.SDL_QUIT:
					running = False
				if event.type == sdl2.SDL_KEYDOWN:
					self.input_key_pressed(event.key.keysym.sym, event.key.repeat)
				elif event.type == sdl2.SDL_KEYUP:
					self.input_key_released(event.key.keysym.sym, event.key.repeat)
			self.update()
			GL.glClearColor(0, 0, 0, 1)
			GL.glClear(GL.GL_COLOR_BUFFER_BIT)

			self.renderer.render(self.entities[0].shader.program)

			sdl2.SDL_GL_SwapWindow(self.window)
			sdl2.SDL_Delay(10)

		sdl2.SDL_GL_DeleteContext(self.context)
		sdl2.SDL_DestroyWindow(self.window)
		sdl2.SDL_Quit()
		return 0
if __name__ == '__main__':
	game = Game(800, 600)
	game.loop()
