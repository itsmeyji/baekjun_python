n, m = map(int, input().split())
a = []
b = []

for i in range(n):
  L = list(map(int, input().split()))
  a.append(L)

for i in range(n):
  L = list(map(int, input().split()))
  b.append(L)


for i in range(n):
  for j in range(m):
    print(a[i][j]+b[i][j], end = ' ')