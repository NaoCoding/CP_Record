#include <bits/stdc++.h>

using namespace std;
int main(){

    int t;
    cin >> t;
    while(t--){
        int n,m;
        cin >> n >> m;
        vector<string> pic(n);
        for(int i=0;i<n;i++) cin >> pic[i];

        vector<vector<int>> cnt(4,vector<int>(2,0));
        for(int i=0;i<m;i++) cnt[0][pic[0][i] == 'B'] += 1;
        for(int i=0;i<n;i++) cnt[1][pic[i][0] == 'B'] += 1;
        for(int i=0;i<n;i++) cnt[2][pic[i][m-1] == 'B'] += 1;
        for(int i=0;i<m;i++) cnt[3][pic[n-1][i] == 'B'] += 1;
        
        if(cnt[0][0] && cnt[1][0] && cnt[2][0] && cnt[3][0]){
            cout << "YES\n"; continue; 
        }
        if(cnt[0][1] && cnt[1][1] && cnt[2][1] && cnt[3][1]){
            cout << "YES\n"; continue; 
        }
        cout << "NO\n";




        
    }

}