#include <bits/stdc++.h>
using namespace std;
//TIME COMPLEXITY 0(1)
bool isAnagram(string s, string t){
    if(s.length()!=t.length()){
        return false;
    }
    else{
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if(s==t){
            return true;
        }
        else{
            return false;
        }
    }

}

int main(){
    string s,t;
    cin>> s>>t;
    cout<< isAnagram(s,t)<< endl;
    
    return 0;
}