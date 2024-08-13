#include <bits/stdc++.h>

using namespace std;


int n,m,k;
long long int cnt(int i , int j){

    long long int row = 0 , col = 0;

    for(int a=i-k+1;a<=i;a++) if(a>=0 && a+k<=n) row += 1;
    for(int b=j-k+1;b<=j;b++) if(b>=0 && b+k<=m) col += 1;
    return row * col;

}

int main(){
    int t;
    cin >> t;
    while(t--){
        
        cin >> n >> m >> k;
        long long int w;
        cin >> w;
        vector<int> gols(w);
        for(long long int i=0;i<w;i++) cin >> gols[i];
        sort(gols.begin(),gols.end());
        reverse(gols.begin(),gols.end());
        priority_queue<long long int> pq;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
    
                pq.push(cnt(i,j));
            }
        }
        
        long long int ans = 0;
        for(int i=0;i<gols.size();i++){
            //cout << ans << endl;
            //cout << pq.top()  << " " << gols[i] << endl;
            ans += gols[i] * pq.top();
            pq.pop();
        }
        cout << ans << endl;
    }
}