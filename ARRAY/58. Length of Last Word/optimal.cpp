#include <bits/stdc++.h>
using namespace std;

int main(){
    string s="Hello Bro   ";
    int count=0;
    for(int i=s.length()-1;i>=0;i--){
        
        if(s[i]==' ' && count>0){
            break;
        }
        if(s[i]!=' '){
            count++;
        }
    }
    cout<< count<<endl;
    return 0;
}

//O(n)