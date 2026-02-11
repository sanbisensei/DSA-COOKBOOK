#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin>> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    vector<int> newarr;
    for(int i=0; i<n*2;i++){
        if(i<n){
            newarr.push_back(arr[i]);
        }
        else{
            newarr.push_back(arr[i-n]);
        }
    }
    for(int i: newarr){
        cout<< i<<" ";
    }
    

    return 0;
}