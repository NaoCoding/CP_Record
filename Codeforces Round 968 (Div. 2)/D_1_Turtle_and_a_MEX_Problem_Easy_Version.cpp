#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t--){
        long long int n,m;
        cin >> n >> m;
        long long int ans = 0;
        long long int mean = 1;
        for(int i=0;i<n;i++){
            if(i >= m) break;
            int q;
            cin >> q;
            priority_queue<int, vector<int> ,greater<int>> pq;
            map<int,int> appear;
            for(int j=0;j<q;j++){
                int rr;
                cin >> rr;
                if(!(appear[rr])){
                    pq.push(rr);
                    appear[rr]++;
                }
            }

            int time = 0;
            long long int last = -1;
            while(!pq.empty()){
                
                if(pq.top()-1 != last){
                    time += 1;
                    if(time == 2){
                        break;
                    }
                }
                else{
                    long long int now = pq.top();
                    while(now == pq.top()){
                        pq.pop();
                        if(pq.empty()) break;
                    }

                }
                last += 1;
            }
            mean = max(mean , last + 1);
            

        }

        //printf("%ld\n",mean);
        cout << fixed;
        if(mean <= m) cout << (1+m) * m /2  + (1+mean) * mean / 2 << endl;
        else cout << mean*(m+1) << endl;
    }
}