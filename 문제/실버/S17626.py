n = int(input())
dp = [4] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2,n+1) :
    j = 1
    while j**2 <= i :
        dp[i] = min(dp[i], dp[i-(j**2)] + 1)
        j+=1

print(dp[n])