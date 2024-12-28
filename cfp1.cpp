#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    string s="codeforces";
    unordered_set<char> sets;
    for(int i=0;i<s.length();++i){
        sets.insert(s[i]);
    }
    int t;
    cin>>t;
    for(int i=0;i<t;++i){
        char c;
        cin>>c;
        if(sets.find(c)!=sets.end()){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }

}