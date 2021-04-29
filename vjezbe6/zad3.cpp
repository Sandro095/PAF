#include <iostream>
#include <bits/stdc++.h>
using namespace std;
void sortiranje(int s[],int n)
{
    sort(s, s + n);
    for (int i =1 ; i <= n; ++i)
        cout << " " <<s[i];

}
void zamjena(int s[],int temp,int a,int b,int c)
{
    int i;
    temp=s[c+1];
    s[c+1]=s[c];
    s[c]=temp;
    for (i = a; i <=b; i++)
    {
        cout << ' '<<s[i];
    }

}
void reverse(int s[],int a,int b)
{
int i;
for (i = b; i >=a; i--)
    {
        cout << ' '<<s[i];
    }
}
void printanje(int s[],int a,int b)
{
int i;
for (i = a; i <=b; i++)
    {
        cout << ' '<<s[i];
    }
}
int main() {
    int a, b,c,temp,i;
    a=1;
    b=5;
    c=2;
    int s[b]={};
    
    for (i = a; i <=b; i++)
    {
        s[i]=i;
      

    }
    //printanje
    cout<<" Printanje";
    printanje(s,a,b);
    //reverse
    cout<<"\n Reverse";
    reverse(s,a,b);
    //zamjena
    cout<<"\n Zamjena";
    zamjena(s,temp,a,b,c);
    //sortiranje
    cout<<"\n Sortiranje";
    int n=sizeof(s)/sizeof(s[1]);
    sortiranje(s,n);
  

    return 0;
}
