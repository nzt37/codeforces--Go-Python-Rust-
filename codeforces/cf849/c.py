from collections import deque

def solve():
    n = (int)(input())
    s = (deque)(input())
    while len(s) and s[0] != s[-1]:
        s.pop()
        s.popleft()
    print(len(s))
t = (int)(input())
for _ in range(t):
    solve()