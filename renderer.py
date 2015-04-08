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
	elements = []
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
	offset_bytes = 4
	program = None # hacks
	time = 0.0 # no
	rendering_queue = {}
	# queue:
	# shader_program: (element_count, offset), (element_count, offset), ...
	def __init__(self, vertices=None, elements=None):
		self.load_vertex_data(vertices, elements)
		self.vao = GL.glGenVertexArrays(1)
		print self.vao
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
		verts = []
		for v in vertices:
			verts.extend(v.unwrap())
		vertices = verts
		self.vertexData = numpy.array(vertices, dtype=numpy.float32)
		self.elementData = numpy.array(elements, dtype=numpy.int32)
		if generate_vbos:
			GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo) 
			GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)
			GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ebo)
			GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, self.elementData.nbytes, self.elementData, GL.GL_STATIC_DRAW)
			# is this exactly good way to do this?

	def queue_data(self, vertices, elements, offset_callback):
		to_remove = []
		for v in vertices:
			if v in self.vertices:
				print "duplicate: ", v.x, v.y, v.z
				old_index = vertices.index(v)
				new_index = self.vertices.index(v)
				for i in range(0, len(elements)):
					if elements[i] == old_index:
						elements[i] = new_index
				to_remove.append(v)
		print vertices, elements
		element_indices = []
		for v in vertices:
			if v not in to_remove:
				try:
					element_number = vertices.index(v)
					element_indices.append(element_number)
				except ValueError:
					print "value error"
		element_indices.sort(reverse=True)
		print element_indices
		if len(self.vertices) > 0:
			for ind in element_indices:
				while True:
					try:
						print ".",
						i = elements.index(ind)
					except:
						print i, 
						break
					elements[i] += len(self.vertices) - len(to_remove)
		vertices = [v for v in vertices if v not in to_remove]
		self.queue_vertices(vertices)
		offset_callback.set_offset(len(self.elements))
		self.queue_elements(elements)

	def queue_vertices(self, vertices):
		self.vertices.extend(vertices)

	def queue_elements(self, elements):
		self.elements.extend(elements)

	def queue(self, program, element_count, index_offset):
		if program in self.rendering_queue.keys():
			self.rendering_queue[program].append((element_count, index_offset))
		else:
			self.rendering_queue[program] = [(element_count, index_offset)]

	def setup_vao(self):
		pos = GL.glGetAttribLocation(self.program, "position")
		GL.glEnableVertexAttribArray(pos)
		GL.glVertexAttribPointer(pos, 4, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
		GL.glBindVertexArray(0)

	def render(self):
		self.time += .01
		GL.glClearColor(0, 0, 0, 1)
		GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
		# loop through queue
		for s, q in self.rendering_queue.iteritems():
			#print s, q
			# active shader program
			GL.glUseProgram(s)
			for e in q:
				try:
					GL.glBindVertexArray(self.vao)
					# draw triangle, not very exciting
					GL.glDrawElements(GL.GL_TRIANGLES, e[0], GL.GL_UNSIGNED_INT, ctypes.c_void_p(e[1] * self.offset_bytes))
				finally:
					GL.glBindVertexArray(0)
					GL.glUseProgram(0)
		self.rendering_queue.clear()