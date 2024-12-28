#include<iostream>
#include<stack>
#include<vector>
using namespace std;
class Solution {
public:
bool valid(string s){
    stack<char> op;
    for(int i=0;i<s.length();++i){
        if(s[i]==')' && op.empty()){
            return false;
        }
        if(s[i]=='('){
            op.push(s[i]);
        }
        if(s[i]==')' && !op.empty()){
            op.pop();
        }
    }
    return op.empty();
}
string generateRandomString(int length, const string& characters) {
    string result;
    result.reserve(length);
    
    // Initialize random seed
    srand(static_cast<unsigned int>(time(nullptr)));
    
    for (int i = 0; i < length; ++i) {
        // Pick a random character from the set of characters
        result += characters[rand() % characters.size()];
    }
    
    return result;
}

    vector<string> generateParenthesis(int n) {
        string charac="()";
        int len=2*n;
        vector<string> ans;
        while(ans.size()<2*n-1){
            string res=generateRandomString(len,charac);
            if(valid(res)){
                ans.push_back(res);
            }
            else{
                continue;
            }
        }
    }
};
int main() {
    Solution sol;
    int n = 3;
    vector<string> result = sol.generateParenthesis(n);
    
    cout << "Generated Parenthesis Combinations: " << endl;
    for (const string &str : result) {
        cout << str << endl;
    }

    return 0;
}