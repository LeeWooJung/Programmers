"""
distance : 1 ~ 10^9
len(rocks) : 1 ~ 5*10^4 --> m = len(rocks)
1 <= n <= len(rocks)

1. 완전탐색

1) rocks sort
- O(m*log(m))

2) eliminate rocks
- select mCn rocks --> O(mCn)

3) find distance in remained rocks, start, destination
- O(m)

==> O(m^2 * log(m) * mCn)

2. 다른 방법

Binary Search

1) left, right 값을 정한다.
2) left, right를 이용해서 mid를 구한다. mid = (left + right) // 2
3) mid를 사용해서 [어떤] 기준을 정한다.
    3-1) [어떤] 기준을 만족하면 right = mid(right = mid - 1 등도 가능)로 바꾼다.
        --> mid의 값을 줄이기 위함.
    3-2) [어떤] 기준을 만족하지 못하면 left = mid + 1(left = mid 등도 가능)로 바꾼다.
        --> mid의 값을 증가시키기 위함.

4) mid의 값이 수렴할 때(left <= right)까지 1,2,3 과정을 반복한다.
5) 원하는 값은 mid 이다.

[어떤] 기준 : 제거하는 바위의 개수(count)
- 즉, mid로 제거할 바위의 개수를 정하도록 설정.
- count >= n 이면, 제거해야할 바위의 개수를 줄여야 함. mid를 증가 ==> left = mid + 1
- count < n 이면, 제거해야할 바위의 개수를 늘려야 함. mid를 감소 ==> right = mid - 1

그러면, mid로 제거할 바위의 개수를 어떻게 정할 것인가??

- mid를 거리의 최솟값이라고 가정.
- 시작점부터 시작해서 mid 거리 안에 바위가 있으면 해당 바위를 제거(count 증가)
- 제거되지 않는 바위부터 시작해서 다시 mid 거리 안에 바위가 있으면 해당 바위를 제거(count 증가)
- 제거되지 않는 바위 + mid 거리 >= distance 되면 count return
- cf. mid가 되는 값 중에 최댓값을 찾아야함.

return된 count가 n보다 크다면 최소 거리를 줄여야 함 ==> right = mid - 1 (right = mid 를 사용하면 count의 개수가 n보다 계속 큰 상태로 유지될 수도 있음.)
return된 count가 n보다 작거나 같다면 최소 거리를 늘려야 함 ==> left = mid + 1 (최대가 되는 mid 값을 찾기 위해 left = mid + 1로 계속 증가시킴.)

최소 거리는 1이므로 left = 1, 최대 거리는 distance이므로 right = distance로 설정.

==> O(log(distance) * len(rocks))
"""

def count(rocks, minDist):
    
    c = 0
    start = 0
    
    for i, position in enumerate(rocks):
        
        if rocks[-1] < start + minDist:
            return c + (len(rocks) - i)
            
        if position < start + minDist:
            c += 1
        else: # start + minDist <= position
            start = position
        
    return c

def solution(distance, rocks, n):
    answer = 0
    
    left, right = 1, distance
    
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2
        
        c = count(rocks, mid)
        if c > n:
            right = mid - 1
        else:
            answer = max(mid, answer)
            left = mid + 1
    
    
    return answer