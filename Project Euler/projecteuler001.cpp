#include <iostream>
#include <cmath>

int multiplestf(int);
int specialtriple(int);

int main(){
    int sum = multiplestf(1000);
    std::cout << "The value is " << sum << ".";
    return 0;
}

// Project Euler 1
int multiplestf(int num){
    int sum = 0;
    for(int i = 1; i < num; i++){
        if(i % 3 == 0 || i % 5 == 0)
            sum += i;
    }
    return sum;
}
