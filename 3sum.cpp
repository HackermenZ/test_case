#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int> > threeSum(vector<int>& nums) {
        vector<vector<int> > result;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-2;++i){
            int x=nums[i];
            vector<int> subres;
            int lval,rval;
            bool flag=false;
            int l=i+1,r=nums.size()-1;
            while(l<r){
                if(nums[l]+nums[r]>-x){
                    r--;
                    continue;
                }
                else if(nums[l]+nums[r]<-x){
                    l++;
                    continue;
                }
                else if(nums[l]+nums[r]==-x){
                    lval=nums[l];
                    rval=nums[r];
                    subres.push_back(x);
                    subres.push_back(lval);
                    subres.push_back(rval);
                    flag=true;
                    break;
                }

            }
            if(subres.size()==3){
                result.push_back(subres);
            }
            if(flag){
                auto it1=find(nums.begin(),nums.end(),x);
                auto it2=find(nums.begin(),nums.end(),lval);
                auto it3=find(nums.begin(),nums.end(),rval);
                if(it1!=nums.end()){
                    nums.erase(it1);
                }
                if(it2!=nums.end()){
                    nums.erase(it2);
                }
                if(it3!=nums.end()){
                    nums.erase(it3);
                }

            }
        }
        return result;
    }
};
int main()
{
    Solution s;
    vector<int> num(6),nun(3);
    num[0]=-1;
    num[1]=0;
    num[2]=1;
    num[3]=2;
    num[4]=-1;
    num[5]=-4;
    nun[0]=0;
    nun[1]=1;
    nun[2]=1;
    for(auto x:num){
        cout<<x<<endl;
    }
    vector<vector<int> > out=s.threeSum(nun);
    for(vector<int> y:out){
        cout<<'{';
        for(int x:y){
            cout<<x<<',';
        }
        cout<<'}'<<endl;
    }
}