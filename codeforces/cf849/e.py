from collections import deque

def solve():
    n = (int)(input())
    # a = map(int,input().split())
    a = [int(x) for x in input().split() ]
    # print(a)
    p = 0
    for i in  range(n):
        if a[i] < 0:
            p += 1
            a[i] = -a[i]
    a.sort()
    s = sum(a)
    if p % 2 == 1:
        s -= 2 * a[0]
    print(s)


t = (int)(input())
for _ in range(t):
    solve()