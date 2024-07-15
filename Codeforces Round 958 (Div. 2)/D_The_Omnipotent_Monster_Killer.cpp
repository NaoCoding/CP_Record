#include <bits/stdc++.h>

using namespace std;

int main(){

    int testcase;
    cin >> testcase;
    while(testcase -- ){
        int v;
        cin >> v;
        vector<int> side(v , 0);
        vector<long long int> cost(v);
        for(int i=0;i<v;i++) cin >> cost[i];

        if(v == 1){
            cout << cost[0] << endl;
            continue;
        }

    

        for(int j=0;j<v - 1;j++){
            int a,b;
            cin >> a >> b;
            if(side[a- 1] > 0)side[b- 1] = side[a- 1] == 1 ? 2 : 1;
            else if(side[b- 1]  > 0)side[a- 1] = side[b- 1] == 1 ? 2 : 1;
            else{
                side[a - 1] = 1;
                side[b - 1] = 2;
            }
        }
        //for(int j=0;j<v;j++) cout << side[j] << endl;
        long long int ans[2] = {0};
        for(int j=0;j<v;j++){
            // cout << cost[j] << endl;
            ans[side[j] - 1] += cost[j];
        }
        //cout << ans[0] << " " << ans[1] << endl;
        
        if(ans[0] > ans[1]) cout << ans[1] * 2 + ans[0] << endl;
        else cout << ans[0] * 2 + ans[1] << endl;
    }

}