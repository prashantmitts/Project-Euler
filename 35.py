n = int(input())
def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if not(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l
primes = eratosthenes(n)
l = []
i = 0
ans = 0
while (i < len(primes)):
    k = str(primes[i])
    if (not(k.count('0') > 0 or k.count('2') > 0 or k.count('4') > 0 or k.count('6') > 0 or k.count('8') > 0 or
        k.count('5') > 0)):
        c = len(k)-1
        while (c > 0):
            k = k[1:] + k[0]
            if not(int(k) in primes):
                c = 0
            c -= 1
        if(c != -1):
            ans += primes[i]
    else:
        if(len(k)==1):
            ans += primes[i]
    i += 1
print(ans)
