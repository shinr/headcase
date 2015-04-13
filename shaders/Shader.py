from OpenGL.GL import shaders
from OpenGL import GL
import ctypes
import os
import shaderdb

class Shader:
	program = None
	uniform_location = None
	def __init__(self, vertex_shader=None, fragment_shader=None):
		self.create_shader(vertex_shader, fragment_shader)

	def check_shader(self, program_id, check_type):
		print "checking ", program_id
		print "--------------------"
		length = ctypes.c_int(0)
		data = ctypes.c_int(0)
		if check_type == GL.GL_COMPILE_STATUS:
			GL.glGetShaderiv(program_id, check_type, data);
			if data.value == 0:
				GL.glGetShaderiv(program_id, GL.GL_INFO_LOG_LENGTH, length)
				buff = ctypes.create_string_buffer(length.value)
				written = ctypes.c_int(0)
				GL.glGetShaderInfoLog(program_id, length, None, buff)
				print buff.value
			else:
				print "no errors"

		elif check_type == GL.GL_LINK_STATUS:
			GL.glGetProgramiv(program_id, check_type, data)
			if data.value == 0:
				GL.glGetProgramiv(program_id, GL.GL_INFO_LOG_LENGTH, length)
				buff = ctypes.create_string_buffer(length.value)
				written = ctypes.c_int(0)
				GL.glGetProgramInfoLog(program_id, length, written, buff)	
				print buff.value
			else:
				print "no errors"

	def set_uniform(self, uniform_name):
		self.uniform_location = GL.glGetUniformLocation(self.program, uniform_name)

	def read_shader(self, shader_file):
		shader_path = "./"
		f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), shader_file), 'r')
		contents = f.read()
		f.close()
		return contents

	def create_shader(self, vert_shader, frag_shader):
		if shaderdb.get_shader(vert_shader, frag_shader):
			self.program = shaderdb.get_shader(vert_shader, frag_shader)
			return
		vert = shaders.compileShader(self.read_shader(vert_shader), GL.GL_VERTEX_SHADER)
		self.check_shader(vert, GL.GL_COMPILE_STATUS)

		frag = shaders.compileShader(self.read_shader(frag_shader), GL.GL_FRAGMENT_SHADER)
		self.check_shader(frag, GL.GL_COMPILE_STATUS)

		self.program = GL.glCreateProgram()
		GL.glAttachShader(self.program, vert)
		GL.glAttachShader(self.program, frag)
		GL.glBindFragDataLocation(self.program, 0, "outColor")
		GL.glLinkProgram(self.program)

		self.check_shader(self.program, GL.GL_LINK_STATUS)
		shaderdb.save_shader(vert_shader, frag_shader, self.program)