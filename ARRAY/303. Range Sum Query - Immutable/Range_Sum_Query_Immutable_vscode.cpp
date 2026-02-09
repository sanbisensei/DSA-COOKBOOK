#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> nums(n+1);
    for(int i = 1; i <= n; i++) {
        cin >> nums[i];
    }
    //one base indexing
    vector<int> prefix(n+1);
    prefix[0] = 0;

    for(int i = 1; i <= n; i++) {
        prefix[i] = prefix[i - 1] + nums[i];
    }

    int q;
    cin >> q;
    while(q--) {
        int l, r;
        cin >> l >> r;

        int sum;
        if(l == 0) {
            sum = prefix[r];
        } else {
            sum = prefix[r] - prefix[l - 1];
        }

        cout << sum << endl;
    }

    return 0;
}
