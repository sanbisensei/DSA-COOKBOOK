/*
Given T test cases and in each
test case a number N.
Print its factorial for 
each test case % M
where M = 10^9+7

Constraints
1 <= T <= 10^5
1 <= N <= 10^5
*/


#include<bits/stdc++.h>
using namespace std;
const int M = 1e9+7;


int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>> n;
        long long fact = 1;
        for(int i = 2; i<=n; ++i){
            fact = (fact*i) % M;
        }
        cout << fact << endl;
    }
}


    // O(T*N) = 10^10
    /*
    the thing is ami t=4 nisi then
    n = 5,2,2,4 nisi
    5 er jonno 120 print hobe
    2 er jonno 2
    2 er jonno 2
    4 er jonno ekta kichu ashbe
    BUT the BIG BUT is 
    jodi 2 er result amra agei peye
    thaki tahole abar same kaj korar
    dorkar nei, amra kothao store
    koreo to rakhte pari.
    Thought: amra shob factorial agei
    store kore rakhbo
    GO TO Precomputation_Factorial.cpp
    */


