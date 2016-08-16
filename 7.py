def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if not(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l
l = eratosthenes(200000)
t = int(input())
while (t != 0):
  t -= 1
  n = int(input())
  print(l[n-1])
