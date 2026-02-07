#include <bits/stdc++.h>
using namespace std;

bool isAnagram(string s, string t){
    if(s.length()!=t.length()){
        return false;
    }
    else{
        vector<int> freq(26,0);
        //  shudhu lower case niye kaj korbo
        for(int i=0;i<s.length();i++){
            freq[s[i]-'a']++;
            freq[t[i]-'a']--;
        }
        for(int count : freq){
            if(count!=0){
                return false;
            }
        }
        return true;
    }

}

int main(){
    string s,t;
    cin>> s>>t;
    cout<<isAnagram(s,t)<< endl;
    
    return 0;
}
