#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
int main()
{
    int t;
    queue<int> q;
    q.size
    cin>>t;
    bool flag=false;
    for(int i=0;i<t;++i){
        long int n;
        cin>>n;
        if(n==2){
            cout<<"NO"<<endl;
            continue;
        }
        if(n%2!=0){
            cout<<"YES"<<endl;
            continue;
        }
        for(int j=3;j<n/2;j+=2){
            if(n%j==0){
                cout<<"YES"<<endl;
                flag=true;
                break;
            }
        }
        cout<<"NO"<<endl;

    }
}