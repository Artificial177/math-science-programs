#include <iostream>
#include <cmath>
#include <numeric>

#define pass void(0)

using namespace std;

bool concealedsquare(unsigned long long n);

int main() {
    const unsigned long int min = sqrt(1020304050607080900);
    const unsigned long int max = sqrt(1929394959697989990);
    for(unsigned long int i = min; i <= max; i++){
        if(concealedsquare(i)) {
            cout << i << "\n";
            break;
        }
    }
    return 0;
}

bool concealedsquare(unsigned long long n){
    unsigned long long square = n * n;
    const unsigned int digits[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    unsigned long i = 9;

    while (square > 0){
        auto current = square % 10;
        if (current != digits[i--])
            return false;
        square /= 100;
    }
    return true;
}







