#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    long int res;
    long long int mod=pow(10,9)+7;
    vector<long long int> A(100,1);
    for(int i=0;i<t;++i){
        // long long int n,m;
        // cin>>n>>m;
        // long int ans=1;
        // for(int j=0;j<m;++j){
        //     A[i]*=n;
        // }
        // long long int rslt;
        // res=pow(n,m);
        // rslt=mod%res;
        // cout<<A[i]%mod<<endl;
        int a,b;
        cin>>a>>b;
        long int result=1;
        a=a%mod;
        while(b>0){
            if(b%2==1){
                result=(result*a)%mod;
            }
            else{
            b=b/2;
            a=(a*a)%mod;
            }
        }
        cout<<result<<endl;

    }
}