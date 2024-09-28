#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        long long n , k;
        cin >> n >> k;
        long long m = 0 , sum = 0;
        for(long long i=0;i<n;i++){
            long long x;
            cin >> x;
            m = max(m , x);
            sum += x;
        }
        for(long long i=n;i>=1;i--){
            if((sum+k)/i*i < sum) continue;
            if(m > (sum+k)/i*i/i) continue;
            cout << i << endl;
            break;
        }
    }
}