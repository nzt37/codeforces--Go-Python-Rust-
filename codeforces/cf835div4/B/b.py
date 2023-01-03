T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    p = max(ord(c) for c in s)
    print(p-int(ord('a')+1))