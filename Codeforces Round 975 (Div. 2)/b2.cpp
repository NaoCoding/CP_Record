#include <bits/stdc++.h>

using namespace std;

long long int now=0;
long long int now_count=0;
long long int passed_node=0;
long long int now_flag_index=0;
long long int minuss=0;
long long int n, Q;
long long int arr[100010];
long long int q[100010];

int main(){
    long long int t;
    cin >> t;
    while(t--){
        
        cin >> n >> Q;
        for(long long int i=0;i<n;i++) cin >> arr[i];
    
        for(long long int i=0;i<Q;i++) cin >> q[i];


        now=arr[0];
        now_count=0;
        passed_node=0;
        now_flag_index=0;
        

        unordered_map <long long int, long long int> mp;
        for(long long int i = arr[0];i <= arr[n-1];i++){
            if(i==arr[now_flag_index]){

                passed_node+=1;
                now_flag_index++;
                now_count+=(n-passed_node);

                if(passed_node!=1){
                    minuss=(passed_node-1-1);
                }

                if(passed_node!=1){
                    minuss=passed_node-2;
                }
                
                
            }else{
                if(passed_node!=1){
                    minuss=passed_node-1;
                }
            }
            
            
            long long int minus_value=((1+minuss)*minuss)/2;

            //cout<<"minus= "<<minuss<<endl;
            //cout<<"minus_value= "<<minus_value<<endl;
            //cout<<i<<" is covered "<<(now_count - minus_value)<<" points\n";
            //cout<<"passed points "<<passed_node<<endl<<endl;

            mp[now_count - minus_value]++;

        }
        for(long long int i=0;i<Q;i++){
            cout<<mp[q[i]]<<" ";
        }
    }

    
    return 0;
}