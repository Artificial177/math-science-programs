#include <iostream>
#include <cmath>
#include <numeric>

int smallestmultiple(int);

int main() {
    int ans = smallestmultiple(20);
    std::cout << "The value is " << ans << ".";
    return 0;
}

int smallestmultiple(int bound){
    int mul = 1;
    for(int i = 2; i <= bound; i++){
        mul *= floor(i / std::gcd(mul, i));
    }
    return mul;
}



