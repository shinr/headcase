#version 330
in vec3 position;
uniform vec3 pos;
void main() { 
		gl_Position = vec4(position, 1.0);
		gl_Position = vec4(pos, 1.0);
} 