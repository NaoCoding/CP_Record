#include <bits/stdc++.h>
using namespace std;
int main(){

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        string r;
        cin >> r;
        if(r[0] == r[n-1]) printf("No\n");
        else printf("YES\n");
    }
}