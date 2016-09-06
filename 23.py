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

x1 = {}
i = 1
while (i < 3*10**4):
    if (get(i) > i):
        x1[i] = 1
    else:
        x1[i] = 0
    i += 1

x = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

def ans(n,x):
    if (n in x):
        x[n]
    else:
        i = 12
        while (i < n):
            if (x1[i] + x1[n-i] == 2):
                x[n] = 1
                return 1
            i += 1
        x[n] = 0
        return 0
    
t = int(input())

while (t > 0):
    t -= 1
    n = int(input())
    if (n > 28123):
        print("YES")
    else:
        if (ans(n,x) == 0):
            print("NO")
        else:
            print("YES")
