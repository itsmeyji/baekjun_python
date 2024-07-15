#11650 좌표 정렬하기

rep = int(input())
a = []
for i in range(rep):
  L = list(map(int, input().split()))
  a.append(L)

a.sort(key = lambda x : (x[0], x[1]))

for _ in range(rep):
  print(a[_][0], a[_][1])