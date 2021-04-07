#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main(){
    int t;
    cin>>t;
    while(t--){
        ll n, flag1 = 0, flag = 0 ,count=0;
        cin>>n;
        ll a[n];
        for(ll i = 0; i<n ; i++){
            cin>>a[i];
        }
        for(ll i = 1; i<n ; i++){
            if(a[i-1]>a[i]){
                flag = 1;
                if(count==0){
                    count++;
                    continue;
                }
            }
            if(flag==1){
                if((a[i-1]>a[i]) || a[i]>a[0]){
                    flag1 = 1;
                    break;
                }
            }
        }
        if(flag1==1){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
            if(flag==1){
                cout<<1<<endl;
            }
            else{
                cout<<0<<endl;
            }
        }
        
        
    }
}
