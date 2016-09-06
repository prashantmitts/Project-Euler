def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if not(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l
primes = eratosthenes(334)

def getsum(n,primes):
    i = 0
    ans = 1
    while (i < len(primes)):
        if (n <= 1):
            return ans
        if (n < primes[i]):
            return ans
        if (n%primes[i] == 0):
            c = primes[i]
            k = 0
            while (n%c == 0):
                k += 1
                n = n//c
            ans *= ((c**(k+1) - 1)//(c-1))
        i += 1
    return ans


def get(n):
    if (n == 0):
        return 0
    return getsum(n,primes)-n

i = 1
l = []
while (i <= 10**5):
    l += [get(i)]
    i += 1

n = int(input())
while (n > 0):
    n -= 1
    c = int(input())
    i = 1
    a = 0
    while (i < c):
        k = l[i-1]
        if (k != i):
            if (k <= 10**5):
                k = l[k-1]
            else:
                k = get(k)
            if (k == i):
                a += i
        i += 1
    print(a)
