from OpenGL.GL import shaders
from OpenGL import GL
import ctypes
import os

class Shader:
	program = None
	uniform_location = None
	def __init__(self, vertex_shader=None, fragment_shader=None):
		self.create_shader(vertex_shader, fragment_shader)

	def check_shader(self, program_id, check_type):
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

		elif check_type == GL.GL_LINK_STATUS:
			GL.glGetProgramiv(program_id, check_type, data)
			if data.value == 0:
				GL.glGetProgramiv(program_id, GL.GL_INFO_LOG_LENGTH, length)
				buff = ctypes.create_string_buffer(length.value)
				written = ctypes.c_int(0)
				GL.glGetProgramInfoLog(program_id, length, written, buff)	
				print buff.value

	def set_uniform(self, uniform_name):
		self.uniform_location = GL.glGetUniformLocation(self.program, uniform_name)

	def read_shader(self, shader_file):
		shader_path = "./"
		f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), shader_file), 'r')
		contents = f.read()
		f.close()
		return contents

	def create_shader(self, vert_shader=None, frag_shader=None):
		if vert_shader:
			vert = shaders.compileShader(self.read_shader(vert_shader), GL.GL_VERTEX_SHADER)
			self.check_shader(vert, GL.GL_COMPILE_STATUS)

		if frag_shader:
			frag = shaders.compileShader(self.read_shader(frag_shader), GL.GL_FRAGMENT_SHADER)
			self.check_shader(frag, GL.GL_COMPILE_STATUS)

		self.program = shaders.compileProgram(vert, frag)

		self.check_shader(self.program, GL.GL_LINK_STATUS)