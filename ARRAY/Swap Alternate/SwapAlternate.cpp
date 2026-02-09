// amader alternate element swap korte hobe 

#include <bits/stdc++.h>
using namespace std;

int main(){
    cout<<"size of array: ";
    int n;
    cin>>n;

    int arr[n];
    cout<<"enter array elements below: "<<endl;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"original array:"<<endl;
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    for(int i=0;i<n;i=i+2){
        if(i==n-1){
            break;
        }
        swap(arr[i],arr[i+1]);
    }
    cout<<endl<<"swapped array:"<<endl;
    for(int i=0;i<n;i++){
    
        cout<<arr[i]<<" ";
    }




}