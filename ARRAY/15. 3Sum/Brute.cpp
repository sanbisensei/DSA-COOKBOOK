#include <bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin>>n;
    vector<int> nums(n);
    sort(nums.begin(),nums.end());
    for(int i=0;i<n;i++){
        cin>> nums[i];
    }
    int target;
    cout<<"enter target: ";
    cin>>target;

    vector<vector<int>> ans;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1; j<nums.size();j++){
                for(int k=j+1; k<nums.size();k++){
                    if(nums[i]+nums[j]+nums[k]==target){
                        ans.push_back({nums[i],nums[j],nums[k]});
                       
                }
                }
                
            }
        }
        for(auto vec: ans){
            for(int i: vec){
            cout<<i<<" ";
        }
        cout<< endl;
        }
    
    return 0;
}