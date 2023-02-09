

def solve():
    n,c = list(map(int,input().split()))
    a = list(map(int,input().split()))

    for i,j in enumerate(a):
        a[i] += i + 1
    a.sort()
    an = 0
    for i in range(n):
        c -= a[i]
        if c < 0:
            break
        an += 1
    print(an)
        

t = (int)(input())

for _ in range(t):
    solve()