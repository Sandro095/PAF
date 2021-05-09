#include "header2.hpp"

float Harmonic_Particle::increment_akceleracija(float& t,float &a, Point polozaj,fstream&file) {

	t += dt;
	file << t << ",";
	a = -w * polozaj.x;
	return a;
}
float Harmonic_Particle::increment_brzina(float& pocetna_brzina, float& a,fstream& file) {
	pocetna_brzina += dt * a;
	file << pocetna_brzina << ",";
	return pocetna_brzina;
}
float Harmonic_Particle::increment_udaljenosti(Point& polozaj, float& pocetnab) {
	polozaj.x += pocetnab * dt;
	return polozaj.x;
}
Harmonic_Particle& Harmonic_Particle::method() {
	fstream brzina;
	fstream vrime;
	vrime.open("vrijeme.txt", ios::out);
	brzina.open("brzina.txt", ios::out);
	float t = 0;
	float a=0;
	vector<float>udaljenosti;
	vector<float>akceleracija;
	vector<float>brzine;
	for (int i = 0;i < 400;i++) {
		akceleracija.push_back(increment_akceleracija(t, a,polozaj,vrime));
		brzine.push_back(increment_brzina(pocetna_brzina, a,brzina));
		udaljenosti.push_back(increment_udaljenosti(polozaj, pocetna_brzina));
	}
	pozicija(udaljenosti.back());
	brzina_ispis(akceleracija.back());
	fstream myfile;
	myfile.open("udaljenost.txt", ios::out);
	if (!myfile) {
		cout << "Greska" << endl;
	}
	else {
		for (int i = 0;i < udaljenosti.size();i++) {
			myfile << udaljenosti[i] << ",";
		}
	}
	myfile.close();
	fstream myfile1;
	myfile1.open("akceleracija.txt", ios::out);
	if (!myfile1) {
		cout << "Greska" << endl;
	}
	else {
		for (int i = 0;i < akceleracija.size();i++) {
			myfile1 << akceleracija[i] << ",";
		}
	}
	myfile1.close();

	return *this;
}