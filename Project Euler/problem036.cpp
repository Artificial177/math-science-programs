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

bool ispalindrome(string);

int main(){
    int counter = 0;
    for(int i = 1; i < 1000000; i++){
        string binary {};
        int temp = i;
        while(temp > 0){
            if(temp % 2 == 0) binary.insert(binary.begin(), '0');
            else binary.insert(binary.begin(), '1');

            temp >>= 1;
        }
        string num = to_string(i);
        if(ispalindrome(num) && ispalindrome(binary)){
            cout << num << space << binary << endl;
            counter += i;
        }
    }
    cout << counter << "\n";

    return 0;
}

bool ispalindrome(string num){
    if(num == string(num.rbegin(), num.rend())){
        return true;
    }
    return false;
}






















