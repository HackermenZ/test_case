// #include<iostream>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int main()
// {
//     int t;
//     cin>>t;
//     while(t--){
//         int count=0;
//         int n;
//         cin>>n;
//         vector<int> nums(n);
//         for(int i=0;i<n;++i){
//             cin>>nums[i];
//         }
//         for(int i=0;i<n-1;++i){
//             for(int j=i+1;j<n;++j){
//                 int big;
//                 int small;
//                 int bigi;
//                 int smalli;
//                 if(nums[i]>nums[j]){
//                     big=nums[i];
//                     bigi=i;
//                     small=nums[j];
//                     smalli=j;
//                 }
//                 else{
//                     big=nums[j];
//                     bigi=j;
//                     small=nums[i];
//                     smalli=i;
//                 }
//                 if(nums[i]==nums[j] || (big-small)%2==0){
//                     continue;
//                 }
//                 else{
//                     int add=big+small;
//                     nums[bigi]=add;
//                     count++;
//                     if(bigi==i){
//                         break;
//                     }
//                     else{
//                         continue;
//                     }

//                 }
//             }

//         }
//         cout<<count<<endl;
//     }
// }
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int count = 0;
        int n;
        cin >> n;
        vector<int> nums(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> nums[i];
        }
        int odd = 0;
        int even = 0;
        for (int &it : nums)
        {
            odd += it & 1;
        }
        even = n - odd;
        if (odd == 0 || even == 0)
        {
            cout << 0 << endl;
            continue;
        }
        sort(nums.begin(), nums.end());
        for (int i = n - 1; i >= 0; i--)
        {
            if (nums[i] % 2 == 0)
            {
                continue;
            }
            count = nums[i];

            for (int k = 0; k < n; ++k)
            {
                if (nums[k] % 2 != 0)
                {
                    continue;
                }
                if(count<nums[k]){
                    count+=nums[n-1];
                    even++;
                }
                static_assert(count>nums[k]);
                    count += nums[k];
                    continue;
                count += nums[n-1];
                even++;
                break;
            }
        }
        cout << even << endl;
    }
}
