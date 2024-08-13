#include <bits/stdc++.h>

using namespace std;

long long int vv = 10000000000;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> a(n);
        for(int i=0;i<n;i++) cin >> a[i];
        int m;
        cin >> m;
        

        for(int i=0;i<m;i++){
            int ok = 1;
            string s;
            cin >> s;
            if(s.size() != n){
                cout << "NO" << endl;
                continue;
            }
            
            map<int,char> a1;
            map<char,long long int> a2;

            for(int j=0;j<n;j++){
                if(a1[a[j]]){
                    if(a1[a[j]] != s[j]){
                        cout << "NO" << endl;
                        ok = 0;
                        break;
                    }
                }
                a1[a[j]] = s[j];
                if(a2[s[j]]){
                    if(a2[s[j]] != a[j] + vv){
                        cout << "NO" << endl;
                        ok = 0;
                        break;
                    }
                }
                a2[s[j]] = a[j] + vv;

            }

            if(ok) cout << "YES" << endl; 
        }
    }
}