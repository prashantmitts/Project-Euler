def pro(l):
  i = 0
  c = 1
  while (i < len(l)):
    c *= int(l[i])
    i += 1
  return c

def ans(l,k):
  c = pro(l[:k])
  m = k
  while (m<len(l)):
      c = max(c,pro(l[m-k:m]))
      m += 1
  return c


t = int(input())
while (t != 0):
  t -= 1
  n,k = map(int,input().split())
  l = list(input())
  print(ans(l,k))
