

def solve():
    n = int(input())
    s = input()
    pos = [0,0]
    for i in s:
        if i == 'U':
            pos[1] += 1
        if i == 'D':
            pos[1] -= 1
        if i == 'L':
            pos[0] -= 1
        if i == 'R':
            pos[0] += 1
        if pos == [1,1]:
            print("YES")
            return
    print("NO")
t = (int)(input())
for _ in range(t):
    solve()