#include <iostream>

using namespace std;

int main()
{

const int Nx = 2;
const int Ny = 3;
double Mat[Nx][Ny];
double q[2];

Mat[0][0] = 2.0;
Mat[0][1] = 3.0;
Mat[0][2] = 2.5;
Mat[1][0] = 1.3;
Mat[1][1] = 3.0;
Mat[1][2] = 2.5;

cout << "Matrica: " << endl;
for (int i = 0; i < Nx; i++)
{
    for (int j = 0; j < Ny; j++)
    {
        cout << Mat[i][j] << "   ";
    }
    cout << endl;
}
cout << endl;


for (int i = 0; i < Nx - 1; i++)
    for (int h = i + 1; h < Nx; h++)
    {
        double t = Mat[h][i] / Mat[i][i];
        for (int j = 0; j <= Nx; j++)
        {
            Mat[h][j] = Mat[h][j] - t * Mat[i][j];
        }
    }


for (int i = Nx - 1; i >= 0; i--)
{
    q[i] = Mat[i][Nx];
    for (int j = Nx - 1; j > i; j--)
    {
        q[i] = q[i] - Mat[i][j] * q[j];
    }
    q[i] = q[i] / Mat[i][i];
}

cout << "rješenje sustava: " << endl;
cout << q[0] << endl;
cout << q[1] << endl;


return 0;
}