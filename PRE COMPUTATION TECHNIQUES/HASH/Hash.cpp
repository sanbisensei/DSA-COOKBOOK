#include<bits/stdc++.h>
using namespace std;
const int N = 1e7+10;
int hsh[N];

int main(){
    int n;
    cin>> n;
    int a[n];
    for(int i = 0;i<n;++i){
     cin>> a[i];
     hsh[a[i]]++;
    }

    int q;
    cin>> q;
    while(q--){
        int x;
        cin>> x;
        cout << hsh[x] << endl;
    }
}

// O(N) + O(Q*N) = O(N^2) = 10^10 = OLD = SLOW

// O(N) + O(Q) = O(N) = 2*10^5 = NEW = FAST

