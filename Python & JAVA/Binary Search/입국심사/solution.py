# 입국 심사를 기다리는 사람 : 1 ~ 10^9
# 심사관이 한 명을 심사하는 데 걸리는 시간 : 1 ~ 10^9
# 심사관 수 : 1 ~ 10^5

"""
1. 완전 탐색: O(n * len(times)) = O(10^18)
- i번째 사람은 어떤 심사관에게 가야 가장 빨리 끝나는지 확인.
- i번째 사람이 어떤 심사관에게 가면 끝날 때의 시간을 기록.
ex)
times = [7, 10], n = 6
1) canStart = [0, 0], n = 6
    --> canEnd(7, 10)
2) canStart = [7, 0], n = 5
    --> canEnd(14, 10)
3) canStart = [7, 10], n = 4
    --> canEnd(14, 20)
4) canStart = [14, 10] , n = 3
    --> canEnd(21, 20)
5) canStart = [14, 20], n = 2
    --> canEnd(21, 30)
6) canStart = [21, 20], n = 1
    --> canEnd(28, 30)
7) canStart = [28, 20], n = 0

2. 더 빠른 방법 필요.

1) 최소, 최대 시간 계산

- 최소로 걸리는 시간: ? --> Assume times = [1, ... , 1]
                      --> n // len(times) + 1 ==> left
- 최대로 걸리는 시간: max(times) * n ==> right

2) Binary Search

- mid = (left + right) // 2
- mid 시간이 걸렸다고 가정. 이 때, 심사 가능한 사람의 수 확인.
- if times[0] = t1
  --> mid // t1 만큼의 사람이 0번째 심사관에게 심사를 받음.
  ==> for time in times : nPeople += mid // time
- if nPeople >= n : 시간이 너무 많이 주어진 것
    ==> mid를 줄여야 함.
    ==> right = mid
- if nPeople < n : 시간이 너무 적게 주어진 것
    ==> mid를 늘려야 함.
    ==> left = mid + 1
- left < right 일 때까지 반복.
- answer = left 

* 시간 복잡도

- 탐색 범위 : max(times) * n ==> O(log(n*max(times)))
- 탐색을 진행할 때마다, 각 심사관이 심사할 수 있는 사람의 수를 확인 ==> O(len(times))

==> O(m * log(n*max(times)))
"""

def checkNumber(n, times, mid):
    
    nPeople = 0
    for time in times:
        nPeople += mid // time
        if nPeople >= n:
            return True
    return False

def solution(n, times):
    answer = 0
    
    m = len(times)
    
    left = n // m + 1
    right = max(times) * n
    
    while left < right:
        
        mid = (left + right) // 2
        
        if checkNumber(n, times, mid):
            right = mid
        else:
            left = mid + 1
            
    answer = left
    
    
    return answer