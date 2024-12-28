#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        bool flag=false;
        vector<int> v(n);
        for(int i=0;i<n;++i){
            cin>>v[i];
        }
        int sum=0;
        for(int i=0;i<n;++i){
            sum+=v[i];
            if(sum%2!=0){
                flag=true;
            break;
        }
        }
        if(flag){
            cout<<"YES"<<endl;
        }
        
        else{
            cout<<"NO"<<endl;
        }
    }
}