def ans(l,i):
    if (len(l) == 1):
        k = l[0]
        return (k[i])
    k = l[0]
    l = l[1:]
    return max(ans(l,i),ans(l,i+1)) + k[i]
    

t = int(input())
while (t > 0):
    t -= 1

    n = int(input())
    l = []
    i = 0
    while (i < n):
        l += [list(map(int,input().split()))]
        i += 1
    print(ans(l,0))
