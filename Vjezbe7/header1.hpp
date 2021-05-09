#define PI 3.14
#define dt 1
#define g -9.81
#define x0 1
#define k 7
#define m 5
#define w -1

#include <iostream>
#include <cstdlib>
#include <cmath>
#include <stdio.h>
#include <vector>
using namespace std;

typedef struct {
	float x;
	float y;
}Point;

class Particle {
private:
	float brzina;
	float kut_otklona;
	Point polozaj;
	float increment_udaljenost(float &t, float Vx0);
	float increment_brzine(float&Vy0);
	float increment_visine(Point& polozaj, float& Vy0);
	
public:
	Particle(float brzina, float kut, float x, float y);
	Particle& method();
	void range(float range) {
		cout << "Udaljenost=" << range<<endl;
	}
	void time(float time) {
		cout << "Vrijeme=" << time << endl;;
	}
};
