target = 10**5
l =[1,2,5,10,20,50,100,200]
way = [0]*(target+1)
way[0] = 1

for i in range(len(l)):
    j = l[i]
    while (j <= target):
        way[j] += way[j-l[i]]
        way[j] = way[j]%(10**9 + 7)
        j += 1
    i += 1
    

        
t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    print(way[n])
