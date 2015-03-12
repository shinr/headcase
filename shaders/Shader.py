from pyglet import gl
import ctypes
import os

class Shader:
	program = None
	def __init__(self, vertex_shader=None, fragment_shader=None):
		self.create_shader(vertex_shader, fragment_shader)

	def check_shader(self, program_id, check_type):
		length = ctypes.c_int(0)
		data = ctypes.c_int(0)
		if check_type == gl.GL_COMPILE_STATUS:
			gl.glGetShaderiv(program_id, check_type, data);
			if data.value == 0:
				gl.glGetShaderiv(program_id, gl.GL_INFO_LOG_LENGTH, length)
				buff = ctypes.create_string_buffer(length.value)
				written = ctypes.c_int(0)
				gl.glGetShaderInfoLog(program_id, length, None, buff)
				print buff.value

		elif check_type == gl.GL_LINK_STATUS:
			gl.glGetProgramiv(program_id, check_type, data)
			if data.value == 0:
				gl.glGetProgramiv(program_id, gl.GL_INFO_LOG_LENGTH, length)
				buff = ctypes.create_string_buffer(length.value)
				written = ctypes.c_int(0)
				gl.glGetProgramInfoLog(program_id, length, written, buff)	
				print buff.value

	def read_shader(self, shader_file):
		shader_path = "./"
		f = open(os.path.dirname(os.path.realpath(__file__)) + '\\' + shader_file, 'r')
		contents = f.read()
		string_buffer = ctypes.create_string_buffer(contents)
		shader = ctypes.cast(ctypes.pointer(ctypes.pointer(string_buffer)), ctypes.POINTER(ctypes.POINTER(gl.GLchar)))
		f.close()
		return shader

	def create_shader(self, vert_shader=None, frag_shader=None):
		if vert_shader:
			v = gl.glCreateShader(gl.GL_VERTEX_SHADER)
			vs = self.read_shader(vert_shader)
			gl.glShaderSource(v, 1, vs, None)
			gl.glCompileShader(v)
			self.check_shader(v, gl.GL_COMPILE_STATUS)

		if frag_shader:
			f = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
			fs = self.read_shader(frag_shader)
			gl.glShaderSource(f, 1, fs, None)
			gl.glCompileShader(f)
			self.check_shader(f, gl.GL_COMPILE_STATUS)
		self.program = gl.glCreateProgram()

		gl.glAttachShader(self.program, f)
		gl.glAttachShader(self.program, v)
	
		gl.glLinkProgram(self.program)
		
		self.check_shader(self.program, gl.GL_LINK_STATUS)