#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    int sum =0;
  
    for(int i=0; i<s.size()-1;i++){
        
        int temp = abs(((int)s[i])-((int)s[i+1]));
        sum = sum + temp;
    }
    cout<< sum << endl;
    
    return 0;
}