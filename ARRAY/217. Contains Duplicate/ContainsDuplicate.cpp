#include <bits/stdc++.h>
using namespace std;

bool CheckDuplicate(vector<int>& v){
    unordered_set<int> seen;
    for(int i:v){
        if(seen.count(i)) {
         return true;
        }
        seen.insert(i);
    }
    return false;
}


int main(){
    vector<int> v={1,2,7,1,5};
    cout<<CheckDuplicate(v)<<endl;



    return 0;
}