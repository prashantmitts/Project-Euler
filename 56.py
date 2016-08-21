def dsum(n):
    a = 0
    while(n != 0):
        a += n%10
        n = n//10
    return a

n = int(input())
k = 0
i = 1
j = 1
while (i < n):
    j = 1
    while (j < n):
        k = max(k,dsum(i**j))
        j += 1
    i += 1
print(k)
