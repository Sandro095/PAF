#include "header1.hpp"

Particle::Particle(float brzina, float kut, float x, float y) {
	this->brzina = brzina;
	kut_otklona = kut;
	polozaj.x = x;
	polozaj.y = y;
	
}
float Particle::increment_udaljenost(float& t,float Vx0) {
	t += dt;
	return Vx0 * t;
}
float Particle::increment_brzine(float& Vy0) {
	Vy0 = Vy0 + g * dt;
	return Vy0;
}
float Particle::increment_visine(Point& polozaj, float& Vy0) {
	polozaj.y = polozaj.y + Vy0 * dt;
	return polozaj.y;

}
Particle& Particle::method() {
	float t = 0;
	vector<float> visine;
	vector<float> udaljenosti;
	vector<float>brzineY;
	vector<float>brzineX;
	float Vy0 = brzina*sin(kut_otklona * (PI / 180));
	float Vx0 = brzina * cos(kut_otklona * (PI / 180));
	for (int i = 0;i < 1000;i++) {
		udaljenosti.push_back(increment_udaljenost(t, Vx0));
		brzineY.push_back(increment_brzine(Vy0));
		visine.push_back(increment_visine(polozaj, Vy0));
		if (polozaj.y < 0)
			break;
	}
	range(udaljenosti.back());
	time(t);
	return *this;
}
