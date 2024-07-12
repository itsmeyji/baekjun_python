#25191 치킨댄스
c = int(input())
coke, beer = map(int, input().split())

N = coke // 2 + beer
if N > c: 
  print(c)
else:
  print(N)