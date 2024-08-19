# 심사자: 1 ~ 10^9
# 심사관: 1 ~ 10^5
# 심사걸리는 시간: 1 ~ 10^9

"""
1. 심사까지 걸리는 최대 시간

- 심사자 * 심사걸리는 시간 = 10^9 * 10^9 = 10^18 = (10^3)^6 = 2^60

2. 탐색

- square = 60 --> 0
- t = 0
- time = 1 << square 부터 탐색

for square in range(60, -1, -1)

answer = t + 1 << square

- 해당 answer 주어졌을 때 심사 가능한 사람이 n 보다 크면,
    - answer이 최소 시간인지 확인해야함.
        - answer -= 1 하고 심사 가능한 사람이 n 보다 작은지 확인.
        - 심사 가능한 사람이 n보다 작으면 answer이 최소 시간임. ==> return answer
        - 심사 가능한 사람이 n보다 크면 answer은 최소 시간이 아님.

- 해당 answer이 주어졌을 때 심사 가능한 사람이 n 보다 작으면,
    - answer 는 더 커져야함.
    - t = answer로 t에 answer를 저장하고, answer보다 더 작은 수들을 더해주면서 확인.

3. 시간 복잡도

- 각 answer time 때 심사 가능한 인원 확인(count function) : O(len(times))
- 최대 bit가 60bit 이므로 확인 해야 하는 bit 수: 60(digit) : O(digit)

==> O(digit * len(times))
"""

def count(time, times):

    c = 0
    for t in times:
        c += time // t

    return c

def solution(n, times):
    answer = 0

    t = 0
    for square in range(60, -1, -1):
        answer = t + (1 << square)

        if count(answer, times) >= n:
            if count(answer - 1, times) < n:
                return answer
            
        else: #count < n
            t = answer

    return answer