#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;++i){
        int n;
        int count=0;
        cin>>n;
        int root=sqrt(n);
        for(int j=1;j<=root;++j){
            if(n%j==0){
                count++;
            if(j!= n/j){
                count++;
            }
            }
        }
        cout<<count<<endl;
    }
}