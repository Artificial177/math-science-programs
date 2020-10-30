#include <iostream>
#include <fstream>
#include <cmath>
#include <numeric>
#include <list>
#include <vector>
#include <string>

#define pass void(0)
#define space " "

using namespace std;

// I'm not so sure if this is a perfect way to do it, but it runs in under a second.

unsigned long long int reversenum(unsigned long long int);
bool ispalindrome(unsigned long long int);
bool islychrel(unsigned long long int, unsigned long long int);
int lychrelnums();

int main(){
    cout << endl << lychrelnums();
    return 0;
}

int lychrelnums(){
    int counter = 0;
    for(unsigned long long int i = 1; i <= 10000; i++){
        unsigned long long int num = i;
        if(islychrel(num, i))
            counter++;
    }
    return counter;
}

bool islychrel(unsigned long long int num, unsigned long long int i){
    for(unsigned long long int j = 1; j <= 50; j++){
        unsigned long long int newnum = num + reversenum(num);
        if(ispalindrome(newnum)) {
            return false;
        }
        num += reversenum(num);
    }
    return true;
}

bool ispalindrome(unsigned long long int num){
    if(num == reversenum(num))
        return true;
    return false;
}

unsigned long long int reversenum(unsigned long long int n){
    unsigned long long int r = 0;
    while(n > 0){
        r = r * 10 + n % 10;
        n = n / 10;
    }
    return r;
}

















