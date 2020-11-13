#include <iostream>
#include <cmath>

#define pass void(0)
#define space " "

using namespace std;

int getdivisors(unsigned int);

int main(){
    int tri = 0;
    int i = 1;
    while(getdivisors(tri) < 500){
        tri += i;
        i++;
    }
    cout << tri << endl;
    return 0;
}

int getdivisors(unsigned int n){
    int count, i;
    count = i = 2;
    while(pow(i, 2) < n){
        if(n % i == 0)
            count += 2;
        i++;
    }
    if(pow(i, 2) == n)
        count++;
    return count;
}





















