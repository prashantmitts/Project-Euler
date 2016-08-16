import math
def ans(n):
    c = 1
    p = -1
    while (c < n):
        k1 = n-c
        k2 = c*c
        k3 = k1*k1 - k2
        k4 = k2-k3
        if (k4 >= 0):
            k5 = int(math.sqrt(k4))
            if (k5*k5 == k4):
                a = (k1-k5)//2
                b = (k1+k5)//2
                if (b > a):
                    if (c > b):
                        p = max(p,(c*(k1+k5)*(k1-k5))//4)
        c += 1
    return p

t = int(input())
while (t != 0):
    t -= 1
    n = int(input())
    print(ans(n))
