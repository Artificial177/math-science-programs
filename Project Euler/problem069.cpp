#include <iostream>

#define pass void(0)
#define space " "

using namespace std;

int main(){
    const unsigned int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
    unsigned int cases = 1000000;
    unsigned int n = 1; unsigned int k = 0;
    while(primes[k] * n <= cases)
        n *= primes[k++];
    cout << n << endl;
}
