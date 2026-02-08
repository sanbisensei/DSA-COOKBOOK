#include <bits/stdc++.h>
using namespace std;
/*
Given array a of n integers. Given Q queries
and in each query given L and R print sum of array
elements from index L to R(L,R included)

Constraints
1<= N <= 10^5
1<= a[i] <= 10^9
1 <= Q <= 10^5
1 <= L,R <= N
*/
const int N = 1e5+10;
int a[N];
int prefixSum[N];


int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        prefixSum[i] = prefixSum[i-1]+ a[i];
    }
    int q;
    cin>>q;
    while(q--){
        int l,r;
        cin>>l>>r;
       cout << prefixSum[r] - prefixSum[l-1] << endl;
    }

    // O(N) + O(Q*N) = 10^10 = OLD
    // O(N) + O(Q) = 10^5 = NEW
        


    return 0;
}