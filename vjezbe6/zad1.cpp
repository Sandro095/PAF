#include <iostream>

int main() {
    double x1, y1, x2, y2;
    x1=2;
    y1=3;
    x2=6;
    y2=5;
    double k, l;
    k= (y2-y1)/(x2-x1);
    l= -x1 +y1;
    std :: cout <<"y="<<k <<"x+"<<l<<".";
    return 0;
}