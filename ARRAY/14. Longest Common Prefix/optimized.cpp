#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<string> str{"flower","flow","flight"}; 

    if(str.empty()){
        cout<<""<<endl;
    }
    sort(str.begin(),str.end());
    string first = str.front();
    string last = str.back();

    int i=0;
    while(i<first.size() && i<last.size() && first[i]==last[i]){
        i++;
    }

    cout<<first.substr(0,i)<<endl;
    
    return 0;
}