from OpenGL import GL
import ctypes
import numpy
import math

class Renderer:
	vao = None
	vbo = None
	vertices = []
	vertexData = numpy.array([
		0.0, 0.5, 0.0, 1.0,
		0.5, -0.366, 0.0, 1.0,
		-0.5, -0.366, 0.0, 1.0,
		1.0, 0.0, 0.0, 1.0,
		0.0, 1.0, 0.0, 1.0,
		0.0, 0.0, 1.0, 1.0,
	], dtype=numpy.float32)
	program = None
	uniColor = 0.0
	time = 0.0
	def __init__(self):
		
		self.vao = GL.glGenVertexArrays(1)
		GL.glBindVertexArray(self.vao)
		self.vbo = GL.glGenBuffers(1)
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
		GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)
		#GL.gl

	def setup_vao(self):
		pos = GL.glGetAttribLocation(self.program, "position")
		GL.glEnableVertexAttribArray(pos)
		#GL.glEnableVertexAttribArray(1)
		GL.glVertexAttribPointer(pos, 4, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
		#GL.glVertexAttribPointer(1, 4, GL.GL_FLOAT, GL.GL_FALSE, 0,
		#ctypes.c_void_p(48))
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
		GL.glBindVertexArray(0)

	def render(self, program):
		self.time += .01
		
		GL.glClearColor(0, 0, 0, 1)
		GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

		# active shader program
		GL.glUseProgram(program)

		try:
			GL.glBindVertexArray(self.vao)

			# draw triangle
			GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
		finally:
			GL.glBindVertexArray(0)
			GL.glUseProgram(0)