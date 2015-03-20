from pyglet import gl
import ctypes

class Renderer:
	vao = ctypes.c_uint(0)
	vbo = ctypes.c_uint(0)
	vertices = []
	program = None
	def __init__(self):
		pass

	def create(self):
		gl.glGenVertexArrays(1, ctypes.byref(self.vao))
		gl.glBindVertexArray(self.vao)
		gl.glGenBuffers(1, self.vbo)
		gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)

	def queue(self, *objects):
		for o in objects:
			self.vertices.extend(o.vertices)
		self.program = o.shader.program
		gl.glUseProgram(self.program)
		pos = gl.glGetAttribLocation(self.program, "position")
		gl.glEnableVertexAttribArray(pos)
		gl.glVertexAttribPointer(pos, 2, gl.GL_FLOAT, gl.GL_FALSE, 0, 0)
		self.construct_vbo()
		

	def construct_vbo(self):
		data = (gl.GLfloat * len(self.vertices))(*self.vertices)
		gl.glBufferData(gl.GL_ARRAY_BUFFER, len(self.vertices), data, gl.GL_STATIC_DRAW)	

	def construct_vao(self):
		pass

	def render(self):
		gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
		
		gl.glLoadIdentity()
		#gl.gluLookAt(5.0,5.0,5.0, 0.0,0.0,0.0,0.0,1.0,0.0)
		gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(self.vertices))
