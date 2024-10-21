"""
Dynamic Programming

1. initialization
- N <== length of Triangle
- dp[N][N]
- dp[i][j] (0 <= j <= i, 0 <= i <= N-1) = triangle[i][j]

2. make reference relation
- dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j]), if i >= 1 and j >= 1
- dp[i][j] = triangle[i][j] + dp[i-1][j], if j == 0
- dp[i][j] = triangle[i][j], if i == j == 0

3. Restriction
- triangle height <= 500, triangle element <= 9999
- maximum of sum = 500 * 9999 = 4999500 < MAX INTEGER
"""

def solution(triangle):
    answer = 0
    
    N = len(triangle)
    # initialization
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            dp[i][j] = triangle[i][j]
            
    
    # Dynamic Programming
    for i in range(1, N):
        dp[i][0] = triangle[i][0] + dp[i-1][0] # j = 0
        for j in range(1, i+1):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
    answer = max(dp[N-1])
    
    return answer