#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
int main()
{
    queue<int> q;
    q.size();
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i=0;i<n;++i){
        cin>>v[i];
    }
    int l=0,r=n-1;
    int sj=0,dm=0;
    int i=1;
    while(l<=r){
        if(i%2!=0){
            if(v[l]>v[r]){
                sj+=v[l];
                l++;
            }
            else{
                sj+=v[r];
                r--;
            }
        }
        else{
            if(v[l]>v[r]){
                dm+=v[l];
                l++;
            }
            else{
                dm+=v[r];
                r--;

            }
        }
        i++;
    }
    cout<<sj<<" "<<dm<<endl;
    
    
}