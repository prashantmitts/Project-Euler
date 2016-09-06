n = int(input())
l = []
while(n > 0):
    l += [input()]
    n -= 1
q = int(input())
while(q > 0):
    q -= 1
    s = input()
    a = 0
    for c in s:
        a += ord(c)-64
    print(a*l.index(s))