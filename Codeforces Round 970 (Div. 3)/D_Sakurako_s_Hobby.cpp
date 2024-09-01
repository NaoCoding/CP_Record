#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> a(n) , color(n);
        for(int i=0;i<n;i++) cin >> a[i];
        for(int i=0;i<n;i++) cin >> color[i];
        

        vector<int> ans(n , -1);
        for(int i=0;i<n;i++){
            int b = color[i] == 0;
            if(ans[i] != -1) continue;
            vector<int> st(1 , i);
            int next = a[i];
            while(st[0] != next - 1){
                st.push_back(next - 1);
                b += color[next - 1] == 0;
                next = a[next - 1];
            }

            for(int j=0;j<st.size();j++) ans[j] = b;
        
            
        }

        for(int i=0;i<n;i++) cout << ans[i] << " ";
        cout << "\n";
    }
}