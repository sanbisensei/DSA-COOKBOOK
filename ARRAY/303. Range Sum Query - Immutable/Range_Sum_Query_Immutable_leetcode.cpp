#include <bits/stdc++.h>
using namespace std;

class NumArray {
public:
    vector<int> prefix;

    NumArray(vector<int>& nums) {
        int n = nums.size();
        prefix.resize(n + 1);
        prefix[0] = 0;

        for(int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + nums[i - 1];
        }
    }
    
    int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
};

int main() {
    vector<int> nums = {-2, 0, 3, -5, 2, -1};

    NumArray obj(nums);

    cout << obj.sumRange(0, 2) << endl;  // 1
    cout << obj.sumRange(2, 5) << endl;  // -1
    cout << obj.sumRange(0, 5) << endl;  // -3

    return 0;
}


//vector diye prefix sum korte gele always vector size dhorte hobe (n+1)