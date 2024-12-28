#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>

int main() {
    std::string str = "Hello, World!";
    if(isalnum(str[6])){
        std::cout<<"YES"<<std::endl;
    }
    
    // Convert the string to lowercase
    std::transform(str.begin(), str.end(), str.begin(), ::tolower);
    
    // Output the result
    std::cout << "Lowercase string: " << (int)('c') << std::endl;

    return 0;
}