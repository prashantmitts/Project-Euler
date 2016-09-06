def pro(l):
    a = 1
    for x in l:
        a *= x
    return a
l = []
i = 0
while (i < 20):
    l += [list(map(int,input().split()))]
    i += 1
ans = 0
i = 0
while (i < len(l)):
    j = 0
    while (j < len(l)-3):
        ans = max(ans,pro((l[i])[j:j+4]))
        j += 1
    i += 1

i = 0
while (i < len(l)-3):
    j= 0
    while (j < len(l)):
        ans = max(ans,((l[i])[j])*((l[i+1])[j])*((l[i+2])[j])*((l[i+3])[j]))
        j += 1
    i += 1


i = 0
while (i < len(l)-3):
    j= 0
    while (j < len(l)-3):
        ans = max(ans,((l[i])[j])*((l[i+1])[j+1])*((l[i+2])[j+2])*((l[i+3])[j+3]))
        j += 1
    i += 1

i = 3
while (i < len(l)):
    j = 0
    while (j < len(l)-3):
        ans = max(ans,((l[i])[j])*((l[i-1])[j+1])*((l[i-2])[j+2])*((l[i-3])[j+3]))
        j += 1
    i += 1

print(ans)
