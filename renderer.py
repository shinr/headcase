from OpenGL import GL
import ctypes
import numpy
import math

class Renderer:
	vao = None
	vbo = None
	vertices = []
	vertexData = numpy.array([
		-0.5, 0.5, 0.0, 1.0,
		0.5, -0.5, 0.0, 1.0,
		-0.5, -0.5, 0.0, 1.0,
		-0.5, 0.5, 0.0, 1.0,
		0.5, 0.5, 0.0, 1.0,
		0.5, -0.5, 0.0, 1.0,
		1.0, 0.0, 0.0, 1.0,
		0.0, 1.0, 0.0, 1.0,
		0.0, 0.0, 1.0, 1.0,
	], dtype=numpy.float32) # this should be created via level generation
	program = None # hacks
	shader = None # hacks
	uniColor = 0.0 # no
	time = 0.0 # no
	def __init__(self, vertices=None):
		self.load_vertex_data(vertices)
		self.vao = GL.glGenVertexArrays(1)
		GL.glBindVertexArray(self.vao)
		self.vbo = GL.glGenBuffers(1)
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
		GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)

	# this should only happen once per level or something
	def load_vertex_data(self, vertices, generate_vbos=False):
		if not vertices:
			return # just use the default data for now
		self.vertexData = numpy.array(vertices, dtype=numpy.float32)
		if generate_vbos:
			GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo) 
			GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)
			# is this exactly good way to do this?

	def setup_vao(self):
		pos = GL.glGetAttribLocation(self.program, "position")
		GL.glEnableVertexAttribArray(pos)
		GL.glVertexAttribPointer(pos, 4, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
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
			GL.glUseProgram(self.shader.program)
			GL.glDrawArrays(GL.GL_TRIANGLES, 3, 3)
		finally:
			GL.glBindVertexArray(0)
			GL.glUseProgram(0)