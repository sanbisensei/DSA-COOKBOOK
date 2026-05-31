#include <bits/stdc++.h>
using namespace std;

int main(){
    pair<int,string> p;
    // p = make_pair(2,"abc");
    p={2,"abul"};
    pair<int,string> p1=p;
    p1.first=69;
    cout<<p1.first;
    cout<<p1.second;
    return 0;
}