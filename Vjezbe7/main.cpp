#include "header1.hpp"

int main(){
    Particle p(7,3,30,4);
    double x = p.range();
    cout << "Range=" << x << endl;
}