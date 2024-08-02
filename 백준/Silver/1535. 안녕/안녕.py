n = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

L, J = [0]+L, [0]+J

dp = [[0 for _ in range(101)] for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, 101):
        if (L[x] <= y):
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-L[x]] + J[x])
        else:
            dp[x][y] = dp[x-1][y]

print(dp[n][99])
