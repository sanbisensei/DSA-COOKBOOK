#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[5] = {1,2,3,4,5};
    vector<int> newarr;
    for(int i=0; i<10;i++){
        
            newarr.push_back(arr[i]);
      
            
    }
    for(int i: newarr){
        cout<< i<<" ";
    }
    

    return 0;
}
