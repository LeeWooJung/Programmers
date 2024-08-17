"""
Problem.
- 연속된 집은 도둑질하지 못함. 따라서 i, i+1 번째 집을 모두 도둑질할 수 는 없음.
- money의 첫 집과 마지막 집은 연결되어 있음(Circular)

initialization
- dp[step]: step 번째 집까지 도둑질했을 때 벌 수 있는 돈의 최댓값.
- dp[] = 0으로 모두 초기화
- N = length of money

make reference relation
1) 첫 번째 집을 도둑질하는 경우: 마지막 집을 도둑질할 수 없음.
- dp[0] = money[0] (무조건 도둑질해야 하므로)
- dp[1] = money[0] (첫 번째 집을 무조건 도둑질하므로)
- dp[step] = max(dp[step-1], money[step] + dp[step-2]) , 2 <= step <= N-2 (마지막 집은 도둑질 할 수 없으므로)
- result: dp[N-2]
2) 첫 번째 집을 도둑질하지 않는 경우: 마지막 집에 대한 도둑질을 신경쓰지 않아도 됨.
- dp[0] = 0 (첫 번째 집을 도둑질하지 않으므로)
- dp[1] = money[1] (두 번째 집을 도둑질할 경우가 최대이므로)
- dp[step] = max(dp[step-1], money[step] + dp[step-2]) , 2 <= step <= N-1
- result: dp[N-1]

1), 2) 중 최댓값 = answer
"""

def solution(money):
    answer = 0

    N = len(money)
    
    # 1. 첫 번째 집을 무조건 도둑질
    dp = [0 for _ in range(N)]
    dp[0] = money[0]
    dp[1] = money[0]

    for step in range(2, N-1):
        dp[step] = max(dp[step-1], money[step] + dp[step-2])

    answer = dp[N-2] # 마지막 집은 도둑질하지 않음.

    # 2. 첫 번째 집을 무조건 도둑질하지 않음.
    dp = [0 for _ in range(N)]
    dp[1] = money[1]

    for step in range(2, N):
        dp[step] = max(dp[step-1], money[step] + dp[step-2])

    answer = max(answer, dp[N-1])

    return answer