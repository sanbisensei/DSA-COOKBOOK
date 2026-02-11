#include <bits/stdc++.h>
using namespace std;

int main() {
    string s = "zaz";
    
    int sum = 0;
    for (int i = 0; i < s.size()-1; i++) {
        sum = sum + abs(((int)s[i]-(int)s[i+1]));
    }
    cout <<sum <<endl;
    

    return 0;
}
