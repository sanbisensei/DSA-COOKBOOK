#include <bits/stdc++.h>
using namespace std;


int main(){
    cout<<"size of array: ";
    int n;
    cin>>n;
    int arr[n];
    cout<< "enter elements: ";
    for(int i=0; i<n;i++){
        cin>> arr[i];
    }
    int target;
    cout<<"enter the target:";
    cin>> target;

    int i=0,j=0;
    long long sum = arr[0];
    int maxLen=0;
    while(j<n){
        while(i<=j && sum>target){
            sum = sum - arr[i];
            i++;
            
        }
        if(target == sum){
            maxLen = max(maxLen,j-i+1);
        }
        j++;
        if(j<n){
            sum = sum + arr[j];
        }
        
    }

    cout<< "max Len is: ";
    cout<< maxLen;
    
    return 0;
}