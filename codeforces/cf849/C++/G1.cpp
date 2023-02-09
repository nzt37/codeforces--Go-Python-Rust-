#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 4;
int n,m;
// int a[maxn];
int b[maxn];
struct node{
    int a,b;
}w[maxn];
void solve() {
    int c;
    cin >> n >> c;
    for(int i = 0; i < n; i++) {
        cin >> w[i].a;
        w[i].b = i + 1;
    }
    sort(w,w+n,[&](node a,node b){
        return a.a+a.b < b.a + b.b;
    });
    int an = 0;
    for(int i = 0; i < n; i++) {
        c -= (w[i].a + w[i].b);

        if(c <= 0) {
            break;
        }
         an ++;
    }
    cout << an << "\n";

} 
int main(){
    int T;
    cin >> T;
    while(T--) {
        solve();
    }
    return 0;
}