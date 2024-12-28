#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    cout<<2<<endl;
    for(int i=3;i<=n;++i){
        bool flag=true;
        for(int j=i-1;j>1;j--){
            if(i%j==0){
                flag=false;
                break;
            }
        }
        if(flag){
            cout<<i<<endl;
        }
    }
}