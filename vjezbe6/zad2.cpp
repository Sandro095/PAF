#include <iostream>
#include <cmath>
#include <cstdio>

int main() {
    double xc, yc, r, x, y;
    double epsilon=0.01;
    xc=1;
    yc=1;
    r=4.2426;
    x=4;
    y=4;
    double dist;
    dist = sqrt(pow(x-xc,2) + pow(y-yc,2));

    
    if (dist<r) {
        printf("nalazi se unutar kruga \n");
    }
    if (dist>r) {
        printf("nalazi se van kruga \n");
    }
    if (fabs(dist-r)<epsilon) {
        printf("nalazi se priblizno na kruznici \n");
    }
    return 0;
}