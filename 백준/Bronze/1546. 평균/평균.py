check = int(input())

a = list(map(int, input().split()))
M = max(a)
for i in range(len(a)):
  a[i] = a[i]/M*100

print(sum(a)/len(a))