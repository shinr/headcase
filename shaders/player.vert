#version 330
in vec4 position;
uniform vec3 pos;
void main() { 
		gl_Position = position + vec4(pos, 1.0);
} 