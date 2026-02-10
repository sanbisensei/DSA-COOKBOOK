#include <bits/stdc++.h>
using namespace std;
//pre-req to solve LC560
/* 
positive array ar target value dawa thakbe.
amader ber korte hobe kon longest sub array target er equal hoy
*/ 

int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    int target;
    cout<<"enter number to match:";
    cin>> target;

    int length = 0;
    

    for(int i = 0; i < n ;i++){
        for(int j = i; j <n;j++){
            int sum = 0;
            for(int k = i ; k<=j;k++){
                sum = sum + arr[k];
            }
            if(sum == target){

                    length = max(length, j-i+1);
                }
        }
        

    }
    cout<< "max length: "<< length<<endl;
}