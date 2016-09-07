import math
l = [1]
a = 1
b = 1
i = 1
c = 1
while (i < 3*10**4):
    if(int(math.log10(a)) > c):
        c = int(math.log10(a))
        l += [i]
    a,b = b,a+b
    i += 1
t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    if (n != 2):
        print(l[n-2])
    else:
        print(7)
