from OpenGL import GL
from player import Player
from renderer import Renderer
import ctypes
#import cyglfw3 as glfw
import sdl2
from sdl2 import video

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
		

	def on_draw(self):		
		self.renderer.render()
		

		# draw ....

	def update(self, dt):
		self.entities[0].update(self.keys)

	def on_key_press(self, button, modifiers):
		if not button in self.keys: 
			self.keys.append(button)

	def on_key_release(self, button, modifiers):
		if button in self.keys: 
			self.keys.remove(button)

	def loop(self):
		event = sdl2.SDL_Event()
		running = True
		while running:
			while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
				if event.type == sdl2.SDL_QUIT:
					running = False

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

#glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, 3);
	#glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, 3);
	#glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE);
	#glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE);
	#glfw.CreateWindow(800, 600, "Jeesus", None, None)