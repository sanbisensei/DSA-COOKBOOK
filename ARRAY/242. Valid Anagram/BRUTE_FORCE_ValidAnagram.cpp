#include <bits/stdc++.h>
using namespace std;

int main(){
    string str1 = "abc";
    vector<char> str1vec;
    for(char x:str1){
        str1vec.push_back(x);    
    }
    

    string str2 = "baa";
    vector<char> str2vec;
    for(char x:str2){
        str2vec.push_back(x);
    }
   
    for(int i=0;i<str1vec.size();i++){
         bool matched = false;
        for(int j=0;j<str2vec.size();j++){
            if(str1vec[i]==str2vec[j]){
                
                str2vec[j] = '#';
                matched = true;
                break;
            }
            }
            if(!matched){
                cout<< "Anagram is not available"<<endl;
                return 0;
            }
    }
    cout<< "Anagram is available"<<endl;
    
    
    ;
    return 0;
}