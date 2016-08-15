def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if not(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l

l = eratosthenes(1000000)

def a(n,k):
    while (n%k == 0):
        n = n//k
    return n
        

def ans(n):
    i = 0
    l1 = []
    while (i < len(l)):
        if (n%l[i] == 0):
            l1 += [l[i]]
            n = a(n,l[i])
        i += 1
    return (l1+[n])

t = int(input())
while (t != 0):
    t -= 1
    n = int(input())
    l1 = (ans(n))
    print(max(l1))
