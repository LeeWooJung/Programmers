def multipleMatrix(mat1, mat2, tot, mod):
    
    # O(tot^3) = O((row*col)^3) = O((n*m)^3)
    mat3 = [[0] * tot for _ in range(tot)]
    for i in range(tot):
        for j in range(tot):
            for k in range(tot):
                mat3[i][j] = (mat3[i][j] + mat1[i][k] * mat2[k][j]) % mod
    return mat3

def matrixSquare(matrix, exponent, tot, mod):
    # 단위 행렬 생성
    result = [[1 if i == j else 0 for j in range(tot)] for i in range(tot)]
    base = matrix

    # Divide and Conquer
    # O(log Exponent) = O(log k)
    while exponent > 0:
        if exponent % 2 == 1:
            result = multipleMatrix(result, base, tot, mod)
        base = multipleMatrix(base, base, tot, mod) # square matrix
        exponent //= 2

    return result

def getKthway(dp, tot, k, mod, nMoves):
    # matrix
    # 경사 수열 d를 만족하며 이동할 때, START: i, END: j 까지 이동하는 방법의 수를 담은 행렬
    matrix = [[dp[nMoves][i][j] % mod for j in range(tot)] for i in range(tot)]
    matrix_k = matrixSquare(matrix, k, tot, mod)

    result = 0
    for x in range(tot):
        for y in range(tot):
            result += matrix_k[x][y]
            result %= mod

    return result

def solution(grid, d, k):
    answer = 0

    row = len(grid)
    col = len(grid[0])
    tot = row * col
    mod = int(1e9 + 7)

    nMoves = len(d)

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    """
    dp[d Order][Start x][Start y][End x][End y] 에서 col의 길이인 m 진법으로 변경
    ==> dp[d Order][(Start x) * m + (Start y)][(End x) * m + (End y)]
    ==> dp[len(d)][n*m][n*m]
    """
    dp = [[[0 for _ in range(tot)] for _ in range(tot)] for _ in range(nMoves + 1)]
    
    # dp initialization
    # 움직이지 않을 때, 한 점이 자신으로 가는 방법 = 1
    for point in range(tot):
        dp[0][point][point] = 1

    # O(len(d) * (n*m)^2)
    for order in range(1, nMoves + 1):
        for start in range(tot):
            cx = start // col
            cy = start % col

            for dx, dy in direction:
                nx = cx + dx
                ny = cy + dy

                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue

                if grid[nx][ny] - grid[cx][cy] != d[order - 1]:
                    continue

                # if electronic cars can move from (cx, cy) - start to (nx, ny) - end using d[order]
                # they can move from previous to end using d[order-1], d[order]
                end = nx * col + ny
                for previous in range(tot):
                    dp[order][previous][end] += dp[order - 1][previous][start]
                    dp[order][previous][end] %= mod

    # O(log k * (n*m)^3)
    answer = getKthway(dp, tot, k, mod, nMoves)
    
    # Total : O(len(d) * (n*m)^2 + log k * (n*m)^3)
    return answer