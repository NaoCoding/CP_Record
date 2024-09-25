#include <bits/stdc++.h>

using namespace std;
int main(){

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        map<int,int> appear;
        priority_queue<int , vector<int> , greater<int>> pq;
        for(int i=0;i<n;i++){
            int q;
            cin >> q;
            if(!appear[q]) pq.push(q);
            appear[q] += 1;
        }
        int now = 0;
        vector<int> f;
        while(!pq.empty()){
            if(pq.top() - now > 1) f.push_back(1);

            else f.push_back(0);
            now = pq.top();
            pq.pop();
        }
        int ans = n % 2;
        int outed = 0;
        for(int i=0;i<f.size();i++){
            if(f[i]){
                outed = 1;
                if(i%2){
                    cout << "Bob\n"; break;
                }
                else{
                    cout << "Alice\n"; break;
                }
            }
        }
        if(!outed) cout << (f.size() % 2 ? "Alice\n" : "Bob\n");
        
    }

}

// Alice Bob
// 1 2 4 6 7 
// 0 0 1 1 0

// 3 5 7 7
// 1 1 1

// 0 1 0 1 0 0 1
// 0 代表會直接拿完
// 1 代表自己拿完或是對方拿完

//1 3
