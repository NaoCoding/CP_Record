#include <bits/stdc++.h>

using namespace std;

int main(){

    int t;
    cin >> t;
    while(t--){
        int n,q;
        cin >> n >> q;
        string a,b;
        cin >> a >> b;
        vector<int> r(n,0);
        vector<int> re(n+1,0);

        map<char,int> appear;
        map<char,int> appear2;

        for(int i=0;i<n;i++){
            appear[a[n]] ++;
            appear[b[n]] --;
            if(appear[a[n]] > 0) r[i] += 1;
            if(i) r[i] += r[i-1];
        }
        for(int i=n-1;i>=0;i--){
            appear2[a[n]] ++;
            appear2[b[n]] -- ;
            if(appear2[a][n] > 0) re[i] += 1; 
            re[i] += re[i+1];
        }

        for(int i=0;i<q;i++){
            int l,r;
            cin >> l >> r;
            cout << appear[r] - appear[l-1] - appear2[r] + appear2[l];
        }
    }

}