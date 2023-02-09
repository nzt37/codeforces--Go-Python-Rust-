import sys
input = sys.stdin.readline

def calc(x):
    ans = 0
    while(x):
        ans += x % 10
        ans //= 10
    return ans


def solve():
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))

    p = [0] * (n + 1)
    def update(idx,val):
        while idx <= n:
            p[idx] += val
            idx += idx & -idx
    

    def query(idx):
        ans = 0
        while idx > 0:
            ans += p[idx]
            idx -= idx & -idx
        return ans
    for _ in range(m):
        b = list(map(int,input().split()))
        if b[0] == 1:
            l = b[1]
            r = b[2]
            update(l,1)
            update(r+1,-1)
        else:
            idx = b[1]
            cnt = query(idx)
            an = a[idx-1]
            for _ in range(cnt):
                if an < 10:
                    break;
                an = sum(map(int, list(str(an))))
            print(an) 



t = (int)(input())

for _ in range(t):
    solve()