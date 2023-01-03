#include <bits/stdc++.h>
using namespace std;

int n,m;
int a[2];
void solve() {
    cin >> a[0] >> a[1] >> a[2];
    sort(a,a+3);
    cout << a[1] << "\n";
}
int main(){
    // int a,b,c;
    int T;
    cin >> T;
    while(T--) {
        solve();
    }
    return 0;
}
