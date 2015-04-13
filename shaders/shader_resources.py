created_shaders = {}

def save_shader(vert, frag, program):
	global created_shaders
	shader_key = vert + frag
	if shader_key in created_shaders.keys():
		return created_shaders[shader_key]
	else:
		created_shaders[shader_key] = program
		return program

def get_shader(vert, frag):
	global created_shaders
	shader_key = vert + frag
	if shader_key in created_shaders.keys():
		return created_shaders[shader_key]
	else:
		return None