#include<iostream>
#include<stack>
using namespace std;
int main()
{
    stack<int> s;

}
///
class Solution {
public:
    bool isValid(string s) {
        stack<char> s1,s2,s3;
        for(int i=0;i<s.length();++i){
            if(s[i]=='('){
                s1.push(s[i]);
            }
            if(s[i]=='{'){
                s2.push(s[i]);
            }
            if(s[i]=='['){
                s3.push(s[i]);
            }
            if(s[i]==')' && !s1.empty()){
                s1.pop();
            }
            if(s[i]=='}' && !s2.empty()){
                s2.pop();
            }
            if(s[i]==']' && !s3.empty()){
                s3.pop();
            }
            if(s[i]==')' && s1.empty()){
                return false;
            }
            if(s[i]=='}' && s2.empty()){
                return false;
            }
            if(s[i]==']' && s3.empty()){
                return false;
            }


        }
        if(s1.empty() && s2.empty() && s3.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};
