t = int(input())
while (t !=0):
    t -= 1
    n = int(input())
    k1 = n*(n+1)//2
    k2 = n*(n+1)*(2*n+1)//6
    print(k1*k1 -k2)
