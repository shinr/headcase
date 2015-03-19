uniform float time;
in vec4 position;
void main() { 
		vec4 v = position;
		v.z = sin(5.0*v.x + time)*0.25;
		gl_FrontColor = vec4(0.0, 0.0, sin(v.z), 1.0); 
		gl_Position = gl_ModelViewProjectionMatrix * v; 
} 