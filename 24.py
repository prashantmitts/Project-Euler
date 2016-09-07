def per(n):
    k = []
    i = 1
    while (i <= 13):
        k =  [(n%i)] + k
        n = n//i
        i += 1
    return k
def a(n):
    n -= 1
    k = per(n)
    l = "abcdefghijklm"
    s = ""
    for c in k:
        c = int(c)
        s += l[c]
        l = l[:c] + l[c+1:]
    return s
t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    print(a(n))
