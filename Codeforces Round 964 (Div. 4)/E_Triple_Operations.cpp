#include <bits/stdc++.h>

using namespace std;
int main(){

    int t;
    cin >> t;
    while(t--){
        int l ; int r;
        long long int answer = 0;

        cin >> l >> r;

        int now = 1;
        while(pow(3,now) <= l){
            now += 1;
        }
        answer = now;
        //cout << answer << " ";

        if(pow(3,now) <= r){
            answer += (pow(3,now) - l) * now;

            while(pow(3,now) <= r){
                now += 1;
                if(pow(3,now) <= r){
                    answer += (pow(3,now) - pow(3,now-1)) * now;
                }
            }   

            answer += ((r+1) - pow(3,now-1)) * now;
        }
        else{
            answer += (r+1-l) * now;
        }


        

        cout << answer << endl;
    }

}