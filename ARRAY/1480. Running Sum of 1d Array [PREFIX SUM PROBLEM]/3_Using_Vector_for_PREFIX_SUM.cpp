#include <bits/stdc++.h>
using namespace std;

vector<int> prefixSum(vector<int> &v){
    vector<int> prefix(v.size());
    for(int i = 0;i<v.size();i++){
        if(i==0){
            prefix[i] = v[i];}
        else{
            prefix[i]= prefix[i-1]+v[i];
        }
    }
    return prefix;

}


int main(){
    vector<int> v= {1,2,3,4,5};
    for(int i : prefixSum(v)){
        cout<<i<<" ";
    
    }
}