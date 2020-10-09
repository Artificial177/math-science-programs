#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

// Probably not the smartest way of doing it. Does take around a minute to complete.
int righttriangle(int);

int main() {
    int j = righttriangle(1000);
    cout << "The value is " << j << ".";
    return 0;
}

int righttriangle(int bound){
    int a = 0;
    int max = 0;
    int current = 0;
    while(a < bound){
        cout << a << endl;
        for(int i = 1; i <= a; i++){
            for(int j = 1; j <= a; j++){
                for(int k = 1; k <= a; k++){
                    if(i + j + k == a){
                        if(pow(j, 2) + pow(k, 2) == pow(i, 2))
                            current++;
                    }
                }
            }
        }
        if(current > max){
            max = a;
        }
        a++;
        current = 0;
    }
    return max;
}





