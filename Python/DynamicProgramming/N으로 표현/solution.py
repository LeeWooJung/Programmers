"""
1. initialization
- dp[1] : N을 1번 사용했을 때 구할 수 있는 수의 집합.
    ==> {N, ...}
- dp[2] : N을 2번 사용했을 때 구할 수 있는 수의 집합.
    ==> {NN, ...}
- dp[3] : N을 3번 사용했을 때 구할 수 있는 수의 집합.
    ==> {NNN, ...}
...
2. Make recurrence relation
- dp[k] = {dp[1] + dp[k-1]} U {dp[1] - dp[k-1]} U {dp[1] * dp[k-1]} U {dp[1] // dp[k-1] if dp[k-1] != 0}
        U {dp[2] + dp[k-2]} U {dp[2] - dp[k-2]} U {dp[2] * dp[k-2]} U {dp[2] // dp[k-2] if dp[k-2] != 0}
        U ...
        U {dp[i] + dp[k-i]} ... <== # 1, 2
"""


def solution(N, number):
    
    if N == number:
        return 1
    
    # initialization
    dp = [set() for _ in range(9)]
    for count in range(1, 9):
        val = int(str(N) * count)
        dp[count].add(val)
    
    # Dynamic Programming
    
    for k in range(1, 9): # dp[k]
        
        for i in range(1, k):
            for left in dp[i]: # 1. dp[i]
                for right in dp[k-i]: # 2. dp[k-i]
                    
                    dp[k].add(left + right) # add
                    if left - right > 0:
                        dp[k].add(left - right) # minus
                    dp[k].add(left * right) # multiply
                    if right > 0:
                        dp[k].add(left // right) # divide
                        
        
        if number in dp[k]:
            return k
        
    return -1