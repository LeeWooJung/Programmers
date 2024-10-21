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
    arr.insert(0, None)  # 인덱스 맞추기 위해 None 추가
    N = len(arr)
    
    # 메모이제이션을 위한 dp와 min_dp 테이블 초기화
    dp = [[None for _ in range(N)] for _ in range(N)]
    min_dp = [[None for _ in range(N)] for _ in range(N)]
    
    # 숫자와 연산자 분리
    for idx in range(1, N, 2):
        arr[idx] = int(arr[idx])

    def get_max(x, y):
        if dp[x][y] is not None:
            return dp[x][y]

        # 구간이 0일 경우
        if x == y:
            dp[x][y] = arr[x]
            return dp[x][y]

        max_value = -int(1e9)
        for z in range(x, y, 2):
            op = arr[z+1]
            if op == "+":
                max_value = max(max_value, get_max(x, z) + get_max(z+2, y))
            elif op == "-":
                max_value = max(max_value, get_max(x, z) - get_min(z+2, y))

        dp[x][y] = max_value
        return dp[x][y]

    def get_min(x, y):
        if min_dp[x][y] is not None:
            return min_dp[x][y]

        # 구간이 0일 경우
        if x == y:
            min_dp[x][y] = arr[x]
            return min_dp[x][y]

        min_value = int(1e9)
        for z in range(x, y, 2):
            op = arr[z+1]
            if op == "+":
                min_value = min(min_value, get_min(x, z) + get_min(z+2, y))
            elif op == "-":
                min_value = min(min_value, get_min(x, z) - get_max(z+2, y))

        min_dp[x][y] = min_value
        return min_dp[x][y]

    return get_max(1, N-1)