#version 330
in vec4 position;
in vec4 color;
out vec4 vertexColor;
uniform vec3 pos;
void main() { 
		gl_Position = position;
		vertexColor = color;
} 