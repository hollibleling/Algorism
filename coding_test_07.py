n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# answer = []
# answer.append(a[0])
# big = a[0]

# for i in range(len(a)-1):
#     if a[i+1] > big:
#         answer.append(a[i+1])
#         big = a[i+1]

# print(answer)
# print(len(answer))
