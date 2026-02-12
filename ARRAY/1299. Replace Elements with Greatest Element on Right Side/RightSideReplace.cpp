#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    int maxNum =-1;
    for(int i=0;i<n;i++){
        cin>> arr[i];
    }
    
    vector<int> newArr(n);
    
    for(int i=n-1; i>=0;i--){
        newArr[i] = maxNum;
        maxNum=max(maxNum,arr[i]);
        
    }
    for(int x: newArr){
        cout<<x<<" ";
    }
    return 0;
}
