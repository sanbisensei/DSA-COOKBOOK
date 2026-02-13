#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> arr1 = {1,2,3,4,3,3,3,5};
    vector<int> arr2 = {1,1,1,3,2,3};

    unordered_set<int> checker(arr1.begin(),arr1.end());
    vector<int> answer;
    for(int x: arr2){
        if(checker.count(x)){
            answer.push_back(x);
            checker.erase(x);
        }
    }

    sort(answer.begin(),answer.end());
    for (int x : answer) {
    cout << x << " ";
}

    
    return 0;
}

//0(n+m)