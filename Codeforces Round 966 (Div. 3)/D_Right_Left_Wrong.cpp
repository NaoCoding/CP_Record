#include <bits/stdc++.h>

using namespace std;

int main(){

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> val(n);
        long long int cur = 0;
        for(int i=0;i<n;i++){
            cin >> val[i];
            cur += val[i];
        }

        string s;
        cin >> s;
        long long int ans = 0;
        
        int l = 0 ,r = n-1;
        while(l < r){
        
            if(s[l] != 'L'){
                cur -= val[l++];
                
                continue;
            }
            if(s[r] != 'R'){
                cur -= val[r--];
                continue;
            }
            //cout << l << " " << r << endl;
            ans += cur;
            cur -= val[l++];
            cur -= val[r--];
            
        }
        cout << ans << endl;
    }

}