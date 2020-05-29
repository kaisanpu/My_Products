import sys
input=sys.stdin.buffer.readline
H,N = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
dp = [10000000000]*(H+1)
dp[0] = 0
for i in range(1,H+1):
    for j in range(N):
        A = ab[j][0]
        B = ab[j][1]
        if i - A < 0:
            dp[i] = min(dp[i],dp[0]+B)
        else:
            dp[i] = min(dp[i],dp[i-A]+B)
print(dp[H])