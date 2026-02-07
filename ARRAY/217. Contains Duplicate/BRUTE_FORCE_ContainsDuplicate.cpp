#include <bits/stdc++.h>
using namespace std;

bool CheckDuplicate(vector<int>& v){
    
    for(int i=0;i<v.size();i++){
        for(int j=i+1;j<v.size();j++){
            if(v[i]==v[j]){
                return true;
            }
            }
    }
    return false;
}


int main(){
    vector<int> v={1,2,7,4,5};

    cout<< CheckDuplicate(v)<<endl;
    return 0;
}
