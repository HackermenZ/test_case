#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--){
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        int count=0;
        if(a>c){
            if(b>d){
                count++;
            }
        }
        if(a>d){
            if(b>c){
                count++;
            }
        }
        if(b>c){
            if(a>d){
                count++;
            }
        }
        if(b>d){
            if(a>c){
                count++;
            }
        }
        cout<<count<<endl;
    }
}