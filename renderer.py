from OpenGL import GL
import ctypes
import numpy
import math
import sys

class Renderer:
	vao = None
	vbo = None
	ebo = None
	vertices = []
	vertexData = numpy.array([
		-0.5, 0.5, 0.0, 1.0,
		0.5, -0.5, 0.0, 1.0,
		-0.5, -0.5, 0.0, 1.0,
		0.5, 0.5, 0.0, 1.0,
		1.0, 0.0, 0.0, 1.0,
		0.0, 1.0, 0.0, 1.0,
		0.0, 0.0, 1.0, 1.0,
	], dtype=numpy.float32) # this should be created via level generation
	elementData = numpy.array([0, 1, 2, 0, 1, 3], dtype=numpy.int32)
	program = None # hacks
	shader = None # hacks
	uniColor = 0.0 # no
	time = 0.0 # no
	def __init__(self, vertices=None, elements=None):
		self.load_vertex_data(vertices, elements)
		self.vao = GL.glGenVertexArrays(1)
		GL.glBindVertexArray(self.vao)
		self.vbo = GL.glGenBuffers(1)
		self.ebo = GL.glGenBuffers(1)
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
		GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)
		GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ebo)
		GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, self.elementData.nbytes, self.elementData, GL.GL_STATIC_DRAW)

	# load new data
	# this should only happen once per level or something
	def load_vertex_data(self, vertices, elements, generate_vbos=False):
		if not vertices:
			return # just use the default data for now
		self.vertexData = numpy.array(vertices, dtype=numpy.float32)
		self.elementData = numpy.array(elements, dtype=numpy.float32)
		if generate_vbos:
			GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo) 
			GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)
			GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ebo)
			GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, self.elementData.nbytes, self.elementData, GL.GL_STATIC_DRAW)
			# is this exactly good way to do this?

	def queue_vertices(self, vertices):
		self.vertices.extend(vertices)

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
			GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, ctypes.c_void_p(0))
			#GL.glUseProgram(self.shader.program)
			#GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, ctypes.c_void_p(0))
		finally:
			GL.glBindVertexArray(0)
			GL.glUseProgram(0)