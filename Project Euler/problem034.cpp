#include <iostream>
#include <cmath>
#include <numeric>
#include <list>
#include <vector>

#define pass void(0)

using namespace std;

unsigned int factorial(unsigned int);
unsigned int digitfactorials(unsigned int);

int main() {
    cout << digitfactorials(1000000);
    return 0;
}

vector<int> separate(unsigned int number){
    vector<int> digits;
    for(number; number > 0; number /= 10){
        digits.push_back(number % 10);
    }
    reverse(digits.begin(), digits.end());
    return digits;
}

unsigned int factorial(unsigned int n){
    if(n == 0)
        return 1;
    if(n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

unsigned int digitfactorials(unsigned int bound){
    unsigned int total = 0;
    for(unsigned int i = 10; i < bound; i++){
        vector<int> digits = separate(i);
        unsigned int sum = 0;
        for(int digit : digits){
            sum += factorial(digit);
        }
        if(sum == i) {
            total += i;
        }
        digits.clear();
        pass;
    }
    return total;
}












