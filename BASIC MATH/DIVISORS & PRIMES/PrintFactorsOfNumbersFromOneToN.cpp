#include <bits/stdc++.h>
using namespace std;

int countDivisors(int n){
    int count=0;
    for(int i=1;i*i<=n;i++){
        if(n%i == 0){
            count++;

            if(i != n/i){
            count++;
        }
        }
    }
    return count;

}


int main(){

    int n;
    cin>>n;
    
    for(int i=1;i<=n;i++){
        cout << countDivisors(i)<< " " <<endl;

    }
    
    return 0;
}