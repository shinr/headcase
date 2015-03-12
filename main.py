from pyglet import gl, window, clock, app, event
import ctypes
import random 

def read_shader(shader_file):
	shader_path = "./shaders/"
	f = open(shader_file, 'r')
	contents = f.read()
	string_buffer = ctypes.create_string_buffer(contents)
	shader = ctypes.cast(ctypes.pointer(ctypes.pointer(string_buffer)), ctypes.POINTER(ctypes.POINTER(gl.GLchar)))
	f.close()
	return shader

class Main(window.Window):
	a = 0.0
	p = None
	loc = None
	myUniformLoc = None
	v = [0.0, 0.0, 0.0, 1.0]
	i = 0
	time = 0.0
	shader1 = None
	shader2 = None
	shader3 = None
	shader4 = None
	shader5 = None
	shader6 = None
	s1loc = None
	s2loc = None
	s3loc = None
	s4loc = None
	s5loc = None
	s6loc = None
	def __init__(self, h, w):
		super(Main, self).__init__(h, w)


	def update(self, dt):
		data = ctypes.c_int(0)
		self.time += dt
		self.s6loc = gl.glGetUniformLocation(self.shader6,"time")
		gl.glGetIntegerv(gl.GL_CURRENT_PROGRAM, data)
		if data.value == self.shader6:
			gl.glUniform1f(self.s6loc, ctypes.c_float(self.time))
		else:
			gl.glUseProgram(self.shader6)
			gl.glUniform1f(self.s6loc, ctypes.c_float(self.time))
			gl.glUseProgram(data.value)



	def draw_cube(self):
		hd = 1.0
		
		gl.glUseProgram(self.shader1)
		
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(-hd,-hd,-hd)
		gl.glVertex3f(-hd,hd,-hd)
		gl.glVertex3f(hd,hd,-hd)
		gl.glVertex3f(hd,-hd,-hd)
		gl.glEnd()
		
		gl.glUseProgram(self.shader2)

		
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(-hd,-hd,-hd)
		gl.glVertex3f(hd,-hd,-hd)
		gl.glVertex3f(hd,-hd,hd)
		gl.glVertex3f(-hd,-hd,hd)
		gl.glEnd()
		
		gl.glUseProgram(self.shader3)
		gl.glUniform1fARB(self.s3loc, self.time);
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(-hd,-hd,-hd)
		gl.glVertex3f(-hd,-hd,hd)
		gl.glVertex3f(-hd,hd,hd)
		gl.glVertex3f(-hd,hd,-hd)
		gl.glEnd()
		
		gl.glUseProgram(self.shader4)
		
	
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(-hd,-hd,hd)
		gl.glVertex3f(hd,-hd,hd)
		gl.glVertex3f(hd,hd,hd)
		gl.glVertex3f(-hd,hd,hd)
		gl.glEnd()
		
		gl.glUseProgram(self.shader6)
		
	
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(-hd,hd,-hd)
		gl.glVertex3f(-hd,hd,hd)
		gl.glVertex3f(hd,hd,hd)
		gl.glVertex3f(hd,hd,-hd)
		gl.glEnd()
		
		gl.glUseProgram(self.shader5)
		
		
		gl.glBegin(gl.GL_QUADS)
		gl.glVertex3f(hd,-hd,-hd)
		gl.glVertex3f(hd,hd,-hd)
		gl.glVertex3f(hd,hd,hd)
		gl.glVertex3f(hd,-hd,hd)
		gl.glEnd()
		

	def on_resize(self, width, height):
		gl.glEnable(gl.GL_DEPTH_TEST)
		gl.glEnable(gl.GL_BLEND)
		gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
		gl.glEnable(gl.GL_CULL_FACE)
		gl.glCullFace(gl.GL_BACK);
		gl.glClearColor(0.2, 0.2, 0.2, 1.0)
		gl.glViewport(0, 0, width, height)
		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		gl.gluPerspective(65, width / float(height), .1, 1000)
		gl.glMatrixMode(gl.GL_MODELVIEW)
		self.load_shaders()
		return event.EVENT_HANDLED	

	def on_draw(self):
		hd = 1.0
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

		gl.glLoadIdentity()
		gl.gluLookAt(0.0,5.0,5.0, 0.0,0.0,0.0,0.0,1.0,0.0)
		gl.glPushMatrix()
		gl.glUseProgram(self.shader3)
		gl.glBegin(gl.GL_TRIANGLE_STRIP)
		gl.glVertex3f(-hd,hd,-3.0)
		gl.glVertex3f(-hd,-hd,-3.0)
		gl.glVertex3f(hd,hd,-3.0)
		gl.glVertex3f(hd,-hd,-3.0)
		gl.glVertex3f(3*hd,hd,-3.0)
		gl.glVertex3f(3*hd,-hd,-3.0)
		gl.glVertex3f(5*hd,hd,-3.0)
		gl.glVertex3f(5*hd,-hd,-3.0)
		gl.glEnd()
		gl.glRotatef(self.a,0,1,0)
		
		self.draw_cube()
		
		gl.glPopMatrix()
		
		self.a+=0.32

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

	def create_shader(self, vert_shader=None, frag_shader=None):
		if vert_shader:
			v = gl.glCreateShader(gl.GL_VERTEX_SHADER)
			vs = read_shader(vert_shader)
			gl.glShaderSource(v, 1, vs, None)
			gl.glCompileShader(v)
			self.check_shader(v, gl.GL_COMPILE_STATUS)

		if frag_shader:
			f = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
			fs = read_shader(frag_shader)
			gl.glShaderSource(f, 1, fs, None)
			gl.glCompileShader(f)
			self.check_shader(f, gl.GL_COMPILE_STATUS)
		program = gl.glCreateProgram()

		gl.glAttachShader(program, f)
		gl.glAttachShader(program, v)
	
		gl.glLinkProgram(program)
		
		self.check_shader(program, gl.GL_LINK_STATUS)

		return program

	def load_shaders(self):
		self.shader1 = self.create_shader("shader.vert", "shader.frag")
		self.shader2 = self.create_shader("shader2.vert", "shader2.frag")
		self.shader3 = self.create_shader("shader3.vert", "shader3.frag")
		self.shader4 = self.create_shader("shader4.vert", "shader4.frag")
		self.shader5 = self.create_shader("shader5.vert", "shader5.frag")
		self.shader6 = self.create_shader("shader6.vert", "shader6.frag")
		gl.glUseProgram(self.shader6)
		self.s6loc = gl.glGetUniformLocation(self.shader6,"time")
		gl.glUseProgram(self.shader3)
		self.s3loc = gl.glGetUniformLocationARB(self.shader3,"time")

		




if __name__ == '__main__':
	m = Main(800, 600)
	clock.schedule_interval(m.update, 1/120.0)
	app.run()

