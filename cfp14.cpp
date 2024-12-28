#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
#include<unordered_set>
using namespace std;
bool compareGreater(const pair<char,int>& a,const pair<char,int>& b){
    return a.second>b.second;
}
int main()
{
    int t;
    cin>>t;
    int maxval=0;
    string ans;
    unordered_map<char,int> map;
    unordered_set<string> sets;
    while(t--){
        string s;
        cin>>s;
        sets.insert(s);
        for(int i=0;i<s.length();++i){
            map[s[i]]++;
        }
    }
    for(auto it:map){
        if(it.second>maxval){
            maxval=it.second;
            ans=it.first;
        }
        else if(it.second==maxval){
            ans+=it.first;
        }
    }
    if(sets.find(ans)!=sets.end()){
        cout<<ans<<endl;
        return 0;
    }
    else{
        sort(ans.begin(),ans.end());
        if(sets.find(ans)!=sets.end()){
            cout<<ans<<endl;
            return 0;
        }
        else{
            sort(ans.begin(),ans.end(),compareGreater);
            cout<<ans<<endl;
        }
    }
}
    
