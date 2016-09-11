def isPal(n):
    k = str(n)
    return (k == k[::-1])

def getadd(n):
    k = str(n)[::-1]
    n1 = int(k)
    return n + n1

def nextpali(n):
    c = 1
    while (c < 60):
        if(isPal(n)):
            return n
        n = getadd(n)
        c += 1
    return 0
    
n = int(input())
i = 1
x = []
y = []
while (i <= n):
    k = nextpali(i)
    if(k != 0):
        if (k in x):
            y[x.index(k)] += 1
        else:
            x += [k]
            y += [1]
    i += 1
m = max(y)
a = x[y.index(m)]
print(a,m)
