#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t--){
        int n, q;
        unsigned long long  arr[100005];
        unsigned long long query[100005];
        cin >> n >> q;
        for(int i = 0;i < n;i++) cin >> arr[i];
        for(int i = 0;i < q;i++) cin >> query[i];
        unordered_map<unsigned long long, unsigned long long> mp;
        for(unsigned long long i = 0;i < n;i++){
            if(i > 0){
				unsigned long long interval = i * (n - i);
				mp[interval] += (arr[i] - arr[i - 1] - 1);	
			}
            unsigned long long cur = (i * (n - i + 1)) - 1; // n - 1
            mp[cur]++;
        }
        mp[n-1] += 1; // add first one
        for(int i = 0;i < q;i++){
            cout << mp[query[i]] << ' ';
        }
        cout << '\n';
    }

    return 0;
}