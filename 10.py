def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if not(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l
l1 = eratosthenes(1000000)

def pre(l):
    l1 = []
    i = 0
    c = 0
    j = 0
    k = l[j]
    while (i <= 10**6):
        if (i == k):
            c += k
            j += 1
            if (j < len(l)):
                k = l[j]
        l1 += [c]
        i += 1
    return l1

l = pre(l1)
t = int(input())
while (t != 0):
    t -= 1
    n = int(input())
    print(l[n])
