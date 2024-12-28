// #include<iostream>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int main()
// {
//     int t;
//     while (t--)
//     {
//         int l,r;
//         cin>>l>>r;
//         vector<int> v(r+1);
//         int count=0;
//         for(int i=l;i<=r;i++){
//             v[i]=i;
//         }
//         for(int i=l;i<=r;++i){
//             int y=v[i];
//             int x;
//             if(v[i-1]==0){
//                 x=0;
//             }
//             x=v[i+1];
//             while (y!=0)
//             {
//                 y=floor(y/3);
//                 x=floor(3*x);
//                 count++;
//             }
//             v[i]=y;
//         }
//         cout<<count<<endl;
//     }
    
// }
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int l, r;
        cin >> l >> r;
        int count = 0;
        vector<int> v;
        
        // Initialize the vector with values from l to r
        for (int i = l; i <= r; ++i) {
            v.push_back(i);
        }
        
        // Perform operations until all elements are zero
        while (!v.empty()) {
            // Sort the vector to always pick the smallest and largest elements
            sort(v.begin(), v.end());
            int x = v.back(); // largest element
            int y = v.front(); // smallest element
            v.pop_back(); // remove largest element
            v.erase(v.begin()); // remove smallest element
            
            // Apply the operation
            int new_x = 3 * y;
            int new_y = y / 3;
            
            // Add the new elements back to the vector if they are not zero
            if (new_x != 0) {
                v.push_back(new_x);
            }
            if (new_y != 0) 
            {
                v.push_back(new_y);
            }
            count++;
        }
        
        cout << count << endl;
    }
    return 0;
}
