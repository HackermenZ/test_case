#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int> nums(n);
    for(int i=0;i<n;++i){
        cin>>nums[i];
    }
    int managedOfficer=0;
    int crime=0;
    int result=0;
    for(int i=0;i<n;++i){
        if(nums[i]>=0){
            managedOfficer+=nums[i];
            continue;
        }
        else if(nums[i]<0){
            if(managedOfficer>=nums[i]*-1){
                managedOfficer+=nums[i];
                continue;
            }
            if(managedOfficer<nums[i]*-1){
                crime+=(nums[i]*-1)-managedOfficer;
            }
        }
    }
    cout<<crime<<endl;
}