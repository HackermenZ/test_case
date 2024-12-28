#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n,s,m;
        cin>>n>>s>>m;
        vector<pair<int,int> > v(n);
        for(int i=0;i<n;++i){
            cin>>v[i].first>>v[i].second;
        }
        if(v[0].first>=s){
            cout<<"YES"<<endl;
            continue;
        }
        bool flag=false;
        for(int i=1;i<n;++i){
            if(v[i].first-v[i-1].second>=s){
                flag=true;
                break;
            }

        }
        if(m-v[n-1].second>=s){
            flag=true;
        }
        if(flag){
            cout<<"YES"<<endl;
            continue;
        }
        
        if(!flag){
            cout<<"NO"<<endl;
            continue;
        }
    }
}