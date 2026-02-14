#include <bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin>>n;
    vector<int> nums(n);
    for(int i=0;i<n;i++){
        cin>> nums[i];
    }
    int target;
    cout<<"enter target: ";
    cin>>target;

    vector<int> ans;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1; j<nums.size();j++){
                if(nums[i]+nums[j]==target){
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }
        for(int i:ans){
            cout<<i<<" ";
        }
    
    return 0;
}

//O(n^2)