#define PI 3.14
#define dt 0.01
#define g 9.81
#define k 7
#define m 5
#define w k/m
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <fstream>
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef struct {
	float x;
	float y;
	float z;
}Point;
class Harmonic_Particle {
private:
	int kut;
	float pocetna_brzina=0;
	Point polozaj;
	float increment_akceleracija(float& t,float&a,Point  polozaj,fstream& file);
	float increment_brzina(float& pocetna_brzina, float& a,fstream&file);
	float increment_udaljenosti(Point&polozaj, float& pocetnab);
public:
	Harmonic_Particle(float a) {
		polozaj.x = a;
	}
	Harmonic_Particle& method();
	void pozicija(float p){
		cout << "Krajnji polozaj je "<<p<< endl;
	}
	void brzina_ispis(float v) {
		cout << "Krajnja akceleracija je " <<v << endl;
	}
};