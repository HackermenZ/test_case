#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool hasDuplicate(vector<int>& nums) {
        vector<int> A(nums.size());
        for(int i=0;i<nums.size();i++){
            A[i]=nums[i];
        }
        auto last=unique(A.begin(),A.end());
        A.erase(last,A.end());
        for(int el:A){
            cout<<el<<endl;
        }
        if(A.size()==nums.size()){
            return false;
        }
        if(A.size()<nums.size()){
            return true;
        }

    }
int main()
{
 int n;
 cin>>n;
 vector<int> B(n);
 for(int i=0;i<n;i++){
    cin>>B[i];
    string s2;
    s2.length();
 }
 cout<<hasDuplicate(B)<<endl;
}