#include <bits/stdc++.h>
using namespace std;

int main(){
    string s="abc";
    string t="ahbgdc";
    int i=0;
    int j=0;
    while(i<s.length() && i<t.length()){
        if(s[i]==t[j]){
            i++;
        }
        j++;
    }
    cout<< (i==s.length())<<endl;
     
    return 0;
}