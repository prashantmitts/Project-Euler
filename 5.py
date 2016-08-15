from fractions import gcd

t = int(input())

l = [1,2,6,12,60]

def ans(n,l):
    k = len(l)
    while (k <= n):
        k += 1
        c = gcd(k,l[k-2])
        l += [(k*l[k-2])//c]
    return l

while (t != 0):
    t -= 1
    n = int(input())
    l = (ans(n,l))
    print(l[n-1])
