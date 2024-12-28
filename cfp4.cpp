#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n;
        int count=0;
        cin>>n;
        string s;
        unordered_map<char,int> map;
        cin>>s;
        for(int i=0;i<s.length();++i){
            map[s[i]]++;
        }
        if(map['A']<=n){
            count+=map['A'];
        }
        else if(map['A']>n){
            count+=n;
        }
        if(map['B']<=n){
            count+=map['B'];
        }
        else if(map['B']>n){
            count+=n;
        }
        if(map['C']<=n){
            count+=map['C'];
        }
        else if(map['C']>n){
            count+=n;
        }
        if(map['D']<=n){
            count+=map['D'];
        }
        else if(map['D']>n){
            count+=n;
        }
        cout<<count<<endl;

    }
}