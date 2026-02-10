#include <bits/stdc++.h>
using namespace std;

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

    int left =0, right = 0;
    long long sum = arr[0];
    int maxLen = 0;
    while(right<n){
        while(left<=right && sum > target){
            sum -= arr[left];
            left++;
        }
        if(sum == target){
            maxLen = max(maxLen, right-left+1);
        }
        right++;  
        if(right<n){sum += arr[right];}
    }
    
    cout << maxLen <<endl;
    return 0;
}


// naked eye = O(n^2)
// actual = O(1)