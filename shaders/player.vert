#version 330
in vec4 position;
in vec4 color;
out vec4 vertexColor;
uniform vec3 pos;
void main() { 
		vertexColor = color;
		gl_Position = position + vec4(pos, 1.0);
} 