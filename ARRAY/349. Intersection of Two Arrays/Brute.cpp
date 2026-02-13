#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> arr1 = {1,2,3,4,3,3,3,5};
    vector<int> arr2 = {1,2,3};

    unordered_set<int> answer;

    for(int x: arr1){
        for(int y: arr2){
            if(x==y){
                answer.insert(y);
                break;
            }
        }
    }

    vector<int> iLoveMyPookie(answer.begin(),answer.end());
    sort(iLoveMyPookie.begin(),iLoveMyPookie.end());
    
    for (int x : iLoveMyPookie) {
    cout << x << " ";
}

    
    return 0;
}