#include <bits/stdc++.h>
using namespace std;

int n,m;
void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int p = -1;
    for(int i = 0; i < n; i++) {
        p = max(p,s[i]-'a'+1);
    }
    cout << p << "\n";
}
int main(){
    int T;
    cin >> T;
    while(T--){
        solve();
    }
    return 0;
}