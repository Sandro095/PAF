#include <iostream>
#include <list>
using namespace std;
#include <bits/stdc++.h>

int main() {
    int a,b;
    a=1;
    b=5;
    set<int> s;
    for(int i=a; i<=b; i++)
    {
        s.insert(i);
        //std::cout << i <<std::endl;
        
    }
    for (auto i = s.begin(); i != s.end(); ++i)
        cout << ' ' << *i;
   for (auto i = s.rbegin(); i != s.rend(); ++i)
        cout << ' ' << *i;
    return 0;
}
