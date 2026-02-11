#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin>>n;
    int count=0;
    
    while(n--){
        int hsh[3] = {0};
        int arr[3];
        for(int i=0;i<3;i++){
            cin>> arr[i];
        }

        for(int i=0;i<3;i++){
            hsh[arr[i]]++;
            
        }
        if(hsh[1]>1){
            count=count+1;
        }

    }
    cout << count << endl;
    return 0;
}
