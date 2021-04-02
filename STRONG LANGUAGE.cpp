#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n, k;
	    cin>>n>>k;
	    string s;
	    cin>>s;
	    int count = 0;
	    int maxv = 0;
	    for(int i = 0;i<n;i++){
	        if(s[i] == '*'){
	            count++;
	            if(count>=maxv)
	                maxv=count;
	        }
	        else
	            count = 0;
	    }
	    if(maxv >= k){
	        cout<<"YES"<<endl;
	    }
	    else
	        cout<<"NO"<<endl;
	
	}
	return 0;
}
