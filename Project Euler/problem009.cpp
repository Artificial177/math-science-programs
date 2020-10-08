#include <iostream>
#include <cmath>

int specialtriple(int);

int main() {
    int triple = specialtriple(1000);
    std::cout << "The Pythagorean Triple is " << triple << ".";
    return 0;
}

int specialtriple(int num){
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num; j++){
            for(int k = 1; k <= num; k++){
                if(pow(j, 2) + pow(k, 2) == pow(i, 2)){
                    if(i + j + k == 1000){
                        return i * j * k;
                    }
                }
            }
        }
    }
    return 0;
}
