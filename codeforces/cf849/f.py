

def calc(x):
    ans = 0
    while(x):
        ans += x % 10
        ans //= 10
    return ans


def solve():
    n,m = list(map(int,input().split))
    a = list(map(int,input().split))

    p = [0] * (n + 1)
    def update(idx,val):
        while idx < n:
            p[idx] = val
            idx += idx & -idx
    

    def query(idx):
        ans = 0
        while idx > 0:
            ans += p[idx]
            idx -= idx & -idx
        return ans

    b = list(map(int,input().split))
    if b[0] == 1:
        update(b[1],1)
        update(b[2],-1)
    else:
        p = query(a[0])
        an = 0
        for _ in p:
            if an < 10:
                break;




t = (int)(input())

for _ in t:
    solve()