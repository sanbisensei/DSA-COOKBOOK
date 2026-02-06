#include <iostream>
using namespace std;

void prefixSum(int arr[],int n){
    int prefix[n] ;
    prefix[0] = arr[0];
    cout << prefix[0] << " ";
    for(int i = 1; i<n;i++){
        prefix[i] = prefix[i-1]+ arr[i];
        cout<< prefix[i] << " ";
    }
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
   
    prefixSum(arr,5);
    return 0;
}
