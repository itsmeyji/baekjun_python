# 백준 9657 돌게임
# 다이나믹 프로그래밍 연습
# 사실 모르겠어서 문제 풀이 방식의 구조를 공부하여 작성함

dp = [0] * 1001
dp[1], dp[2], dp[3], dp[4], dp[5] = "SK", "CY", "SK", "SK", "SK"
stn = [1, 3, 4]

n = int(input())

for i in range(5,n+1):
    for s in stn:
        if dp[i-s] == "CY":
            dp[i] = "SK"
            break
        dp[i] = "CY"

print(dp[n])