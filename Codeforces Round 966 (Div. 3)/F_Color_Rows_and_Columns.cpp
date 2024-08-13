#include <bits/stdc++.h>

using namespace std;
int main(){

    int t;
    cin >> t;
    while(t--){
        int n,k;
        cin >> n >> k;
        priority_queue<pair<int,int> , vector<pair<int,int>>,greater<pair<int,int>>> pq;
        for(int i=0;i<n;i++){
            pair<int,int> f;
            cin >> f.first >> f.second;
            if(f.second < f.first) swap(f.second,f.first);
            pq.push(f);
        }

        long long int ans = 0;
        while(!pq.empty() && k > 0){
            pair<int,int> f = pq.top();
            //cout << f.first << " " << f.second << endl;
            if(k - (f.first + f.second) > 0){
                k -= f.first + f.second;
                ans += f.first * f.second;
            }
            
            else{
                int more = 1;
                while(k){
                    ans += f.first;
                    f.second -= 1;
                    if(f.first > f.second) swap(f.first, f.second);
                    k -= 1;
                }
            }

            pq.pop();
            
            
            //cout << ans << endl;
        }

        if(k > 0) cout << "-1\n";
        else cout << ans+k << endl;

    }
}