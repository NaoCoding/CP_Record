#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        string a;
        cin >> a;
        map<char,int> appear;
        int ava = 0;
        for(auto &i : a){
            appear[i]++;
            if((appear[i]) == 1)ava ++;
        }

        while(ava){
            for(auto &i : appear){
                if(i.second){
                    printf("%c" , i.first);
                    i.second --;
                    if(i.second == 0) ava -= 1;
                }

            }
        }
        printf("\n");



    }
}