"""
1. initialization

- dp[n][m] : 집에서부터 해당 위치까지 이동할 수 있는 방법.
- dp[0][0] = 1
- dp[puddle] = -1 : 이동 불가능

2. make reference relation

- dp[x][y] (Assume there is no puddle)
    = dp[x][y-1] if x == 0
    = dp[x-1][y] if y == 0
    = dp[x-1][y] + dp[x][y-1] if x != 0 and y != 0
"""
def solution(m, n, puddles):
    answer = 0
    
    # initialization
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for col, row in puddles:
        dp[row-1][col-1] = -1 # check puddle
        
    for y in range(m):
        for x in range(n):
            
            if dp[x][y] == -1: # puddle
                continue
            
            if x == 0 and y == 0:
                continue
            elif x == 0:
                dp[x][y] = dp[x][y-1] if dp[x][y-1] != -1 else 0
            elif y == 0:
                dp[x][y] = dp[x-1][y] if dp[x-1][y] != -1 else 0
            else:
                val = 0
                val += dp[x-1][y] if dp[x-1][y] != -1 else 0
                val += dp[x][y-1] if dp[x][y-1] != -1 else 0
                dp[x][y] += val
                
            dp[x][y] %= 1000000007
    
    answer = dp[n-1][m-1]
    
    return answer