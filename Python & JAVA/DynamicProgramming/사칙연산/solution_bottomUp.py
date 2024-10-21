"""
1. initialization

- dp[x][y] : maximum value result of calculation from xth to yth
  (x, y are odd number)
  
- N = len(arr)
- dp[N+1][N+1]
- dp[i][i+2] = arr[i-1] (OP = arr[i]) arr[i+1], i: odd
- dp[i][i] = arr[i], i : odd

2. make reference relation

- dp[x][y] = max (
        dp[x][x] (OP) dp[x+2][y],
        dp[x][x+2] (OP) dp[x+4][y],
        dp[x][x+4] (OP) dp[x+6][y],
        ...
        dp[x][z] (OP) dp[z+2][y],
        ...
        dp[x][y-4] (OP) dp[y-2][y]
        dp[x][y-2] (OP) dp[y][y]
        )
        , where x <= z <= y-2 and x,y,z : odd number
        , x <= z < y

3. Consider conditions

- Minus
==> to make maximum, dp[x][z] (Maximum) - dp[z+2][y] (Maximum) is not correct
==> therefore, we need dp[x][z] (Maximum) - dp[z+2][y] (Minimum) 
    In other words, we need to memorize minimum value

4. Make correct recurrence relation

dp[x][y] = max(dp[x][y], dp[x][z] + dp[z+2][y])
min_dp[x][y] = min(min_dp[x][y], min_dp[x][z] + min_dp[z+2][y])

dp[x][y] = max(dp[x][y], dp[x][z] - min_dp[z+2][y])
min_dp[x][y] = min(min_dp[x][y], min_dp[x][z] - dp[z+2][y])

5-1. Top Down
- dp[1][N-1]: dp[1][a] +/- dp[a+2][N-1]
- dp[1][a]: dp[1][b] +/- dp[b+2][a], dp[a+2][N-1]: dp[a+2][b] +/- dp[b+2][N-1]
...

5-2. Bottom Up
- dp[1][1], dp[3][3], dp[5][5], ... , dp[N-1][N-1] ==> 구간 : 0
- dp[1][3], dp[3][5], dp[5][7], ... , dp[N-3][N-1] ==> 구간 : 2
- dp[1][5], dp[3][7], ... , dp[N-5][N-1] ==> 구간 : 4
...
- dp[1][N-3], dp[3][N-1] ==> 구간: N-4
- dp[1][N-1] ==> 구간: N-2
"""


def solution(arr):
    answer = -1
    
    # initialization
    arr.insert(0, None) # 길이 맞추기.
    N = len(arr)
    dp = [[-int(1e9) for _ in range(N)] for _ in range(N)]
    min_dp = [[int(1e9) for _ in range(N)] for _ in range(N)]

    for idx in range(1, N, 2):
        arr[idx] = int(arr[idx])

    for i in range(1, N, 2): # 구간 = 0
        dp[i][i] = arr[i]
        min_dp[i][i] = arr[i]
    
    for i in range(1, N-2, 2): # 구간 = 2
        
        op = arr[i+1]
        if op == "+":
            dp[i][i+2] = arr[i] + arr[i+2]
            min_dp[i][i+2] = arr[i] + arr[i+2]
        else: # op : "-"
            dp[i][i+2] = arr[i] - arr[i+2]
            min_dp[i][i+2] = arr[i] - arr[i+2]
    
    # dynamic programming

    for t in range(4, N-1, 2): # 구간: 4 ~ N-2
        for x in range(1, N, 2): # 시작 : 1 ~ N-1

            y = x + t
            if y >= N: # 시작 + 구간이 범위를 벗어나면 안됨.
                continue

            for z in range(x, y, 2): # 중간점

                if arr[z+1] == "+":
                    dp[x][y] = max(dp[x][y], dp[x][z] + dp[z+2][y])
                    min_dp[x][y] = min(min_dp[x][y], min_dp[x][z] + min_dp[z+2][y])
                else: # "-"
                    dp[x][y] = max(dp[x][y], dp[x][z] - min_dp[z+2][y])
                    min_dp[x][y] = min(min_dp[x][y], min_dp[x][z] - dp[z+2][y])
    
    
    answer = dp[1][N-1]
    
    return answer