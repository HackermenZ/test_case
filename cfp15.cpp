#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while (t--)
    {
        int a;
        cin>>a;
        string s;
        s=to_string(a);
        if(a>=10001){
            cout<<"NO"<<endl;
            continue;
        }
        else if(s[0]=='1' && s[1]=='0'){
            if(s[2]!='0' && s[2]!='1'){
                cout<<"YES"<<endl;
                continue;
            }
            else{
                cout<<"NO"<<endl;
                continue;
            }
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    
}