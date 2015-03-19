#version 150
uniform float time;
void main() { 
		float alpha = 1.0;
		vec4 newColor = gl_FragCoord;
		newColor.r = sin(newColor.g * 2.0 + time * 2.0);
		alpha = newColor.r;
		gl_FragColor = vec4(newColor.r, 0.0, 0.0, alpha);
		gl_FragColor.a = alpha;
		
} 
