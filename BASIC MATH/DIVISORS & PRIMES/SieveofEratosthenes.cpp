// more efficient way to to solve -
//Print the Prime numbers from 1 to N


/*
1,2,3,4,5,6...100
• I know 2 is a prime number.If 2 is a prime
• then All the multiples of 2 is not prime.
• then I go to 3. 3 is a prime number 
and all the multiples of 3 (6,9 etc) are not prime
*/

#include <bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin>>n;
    vector<int> prime(n+1,1); //assume every one is prime
    prime[1] = 0; // except 1

    

    for(int i=2;i<=n;i++){
        if(!prime[i]) continue;

        // 2i, 3i, 4i
        for(int j=i*i ; j<=n ; j+=i){
         prime[j] = 0;
        }
    }
    
    for(int i = 2; i <= n; i++){
        if(prime[i]){
            cout << i << " ";
        }
    }

    
    return 0;
}

// O( n log(long(n)) ) -> Very Fast -> almost linear