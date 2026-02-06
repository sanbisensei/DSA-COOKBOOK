#include <bits/stdc++.h>
using namespace std;

int Pivot(vector<int>& v)
{
    int n=v.size();
    //calculating the sum of the array
    int rightSum =0;
    for(int i: v){
        rightSum+=i;
    }
    //interate through the array
    int leftSum=0;
    for(int i=0;i<n;i++){
        //update the right sum
        rightSum -= v[i];

        //check if the left sum is equal to the right sum
        if(leftSum == rightSum){
            return i;
        }
        //update the left sum
        leftSum += v[i];
    }
    return -1;
}

int main()
{
	vector<int> v= {1,2,3,0,3};
    cout<<Pivot(v)<<endl;

	return 0;
}