#include <bits/stdc++.h>
using namespace std;
//mail_man will rise
using ll = long long;
constexpr ll mod = 1e9+7;

int main(){
    map<int,int> frq;
    int n;cin>>n;
    
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        frq[x]++;
    }

    for(auto p : frq){
        cout<< p.first << " "<< p.second << endl;
    }

    return 0;
}