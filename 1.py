def ans(k):
    return (k*(k+1))//2

t = int(input())
while (t != 0):
    t -= 1
    n = int(input())
    n -= 1
    k1 = n//3
    k2 = n//5
    k3 = n//15
    print(3*ans(k1)+5*ans(k2)-15*ans(k3))
    
