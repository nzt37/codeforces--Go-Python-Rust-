from collections import deque

def solve():
    n = (int)(input())
    s = input()
    p = [0] * n
    ans = 0
    d = set()
    for i,x in enumerate(s):
        d.add(x)
        p[i] = len(d)
    d = set()
    for i in range(n-1,0,-1):
        # print(i)
        d.add(s[i])
        ans = max(ans,len(d) + p[i-1])
        # print(b)
        
    print(ans)

t = (int)(input())
for _ in range(t):
    solve()