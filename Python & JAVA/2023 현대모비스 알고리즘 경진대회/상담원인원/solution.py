# 멘토 N명, K개 상담 유형
# 참가자가 원하는 상담 유형에 맞는 멘토와 상담
# 참가자가 기다리는 시간 : 참가자가 상담 요청했을 때부터 멘토와 상담을 시작할 때까지의 시간
# 먼저 상담 요청한 참가자가 우선

"""
1.
최대 조합의 개수: n = 20, k = 5일때
- 상담 유형에 최소 한 명씩은 배치되어야 하므로, 배치 조합을 확인할 인원은 최대 15명
- 모든 배치를 확인 해도 15C5 = 3003
- 상담 참가자 최대 300명
- 따라서 최대 3003 * 300 = 900900로 매우 적은 수.
--> 모든 조합을 확인하면서 최소 시간을 확인해도 괜찮음.
--> BackTracking 사용

2.
멘토 중에서 상담을 먼저 끝낸 사람이 바로 다음 사람을 상담할 수 있음.
--> 먼저 상담을 끝낸 멘토를 항상 확인해야함.
--> Priority Queue를 사용할 수 있음.
"""

import heapq
import copy

def backtracking(n, k, start, rest, mentors, request, result):
    
    # 멘토 조합 완성 후, 참가자가 기다리는 시간을 구함.
    if rest == 0:
        
        #print(mentors)
        
        tot = 0
        Mentors = copy.deepcopy(mentors)
        
        for nType in range(k):
            for mentee in request[nType]:
                startTime, mentorLength = mentee
                mentorCanStart = heapq.heappop(Mentors[nType])
                waitTime = max(mentorCanStart - startTime, 0)
                tot = tot + waitTime
                heapq.heappush(Mentors[nType], max(mentorCanStart, startTime) + mentorLength)
                
        return tot
                
        
        
    # 멘토 조합을 위한 BackTracking
    # 멘토들이 상담을 시작하지 않았을 때이므로 멘토들의 상담 끝 시간을 모두 0으로 설정.
    for idx in range(start, len(mentors)):
        
        mentors[idx].append(0)
        returnVal = backtracking(n, k, idx, rest - 1, mentors, request, result)
        result = min(returnVal, result)
        mentors[idx].pop()
        
    return result

def solution(k, n, reqs):
    
    request = {}
    rest = n - k
    
    # 상담유형 1~k까지 0~k-1로 변경하여 key, value(list) 미리 생성.
    for idx in range(k):
        request[idx] = []
    
    for time, length, nType in reqs:
        
        nt = nType - 1 # 상담유형 - 1
        
        request[nt].append([time, length])
    
    answer = backtracking(n, k, 0, rest, [[0] for _ in range(k)], request, 2e9)
    
    return answer