def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if not(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l
primes = eratosthenes(100000)


def getdivisors(n,primes):
    i =0
    ans = 1
    while (i < len(primes)):
        if (n == 1):
            return ans
        if (primes[i] > n):
            return ans
        if (n%primes[i] == 0):
            k = 0
            c = primes[i]
            while (n%c == 0):
                k += 1
                n = n//c
            ans *= (k+1)
        i += 1
    return ans


ll = []
i = 2
while (i < 42000):
    k = i*(i+1)//2
    m = getdivisors(k,primes)
    g = len(ll)
    while (g < m):
        ll += [k]
        g += 1
    if (len(ll) > 10**3):
        i = 45000
    i += 1

t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    print(ll[n-1])
