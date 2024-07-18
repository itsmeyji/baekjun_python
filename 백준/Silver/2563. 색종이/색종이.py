paper = [[0]*100 for _ in range(100)]
rep = int(input())
cnt = 0

for i in range(rep):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[j][k] = 1


for m in range(100):
    for n in range(100):
        if paper[m][n]==1:
            cnt += 1

print(cnt)