#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin>>n;
    vector<int> nums(n);

    for(int i=0; i<n;i++){
        cin>> nums[i];
    }

    vector<int> nuggets;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-1;i++){
            if(nums[i] ==nums[i+1]){
                nuggets.push_back(nums[i]);
            }
        }
    for(int i:nuggets){
        cout << i << " ";
    }



    return 0;
}

