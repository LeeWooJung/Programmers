# temperature: 실외온도
# t1 ~ t2 : 유지해야 하는 온도(t1 < t2)
# a : 실내 != 희망온도 일 때 온도 조절 전력(hope != current)
# b : 실내 == 희망온도 일 때 온도 조절 전력(hope == current)
# onboard : 승객이 탑승 중인 시간

""" Dynamic Programming
1. Initialization
- dp[time][range of temperature]
--> time : 0 ~ onboard length
--> range of temperature: -10 ~ 40 ==> 0 ~ 50 / t1 += 10, t2 += 10, temperature += 10
==> value = max(a, b) * len(onboard)
2. start
dp[0][temperature] = 0
3. bottom up way
- bottom : dp[T1][Current Temp]
--> up : dp[T1 + 1][?]
    ==> 1) hope = off : dp[T1 + 1][nextTemp] = min(dp[T1+1][nextTemp], dp[T1][CurrentTemp])
    ==> 2) hope != current : dp[T1 + 1][nextTemp] = min(dp[T1+1][nextTemp], dp[T1][CurrentTemp] + a)
    ==> 3) hope == current : dp[T1 + 1][nextTemp] = min(dp[T1+1][nextTemp], dp[T1][CurrentTemp] + b)
    
cf) if onboard[T1 + 1] == 1, then nextTemp must be in t1 ~ t2
"""

def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    time = len(onboard)
    maxVal = max(a,b) * time
    nextTemp = 0
    cost = 0
    
    temperature += 10
    t1 += 10
    t2 += 10
    
    dp = [[maxVal for _ in range(51)] for _ in range(time+1)]
    
    dp[0][temperature] = 0
    
    for T in range(time-1):
        
        for curTemp in range(51):
            
            # case 1. hope : off
            if temperature > curTemp:
                nextTemp = curTemp + 1
            elif temperature < curTemp:
                nextTemp = curTemp - 1
            else:
                nextTemp = curTemp
                
            if not(onboard[T+1] == 1 and (nextTemp < t1 or nextTemp > t2)):
                dp[T+1][nextTemp] = min(dp[T+1][nextTemp], dp[T][curTemp])
            
            # case 2 & 3. hope : set, cost a or cost b
            
            for change in [-1, 1, 0]: # 0 means hope == curTemp, others mean hope != curTemp
                nextTemp = curTemp + change
                if nextTemp < 0 or nextTemp > 50:
                    continue
                if change in [-1, 1]:
                    cost = a
                else:
                    cost = b
                
                if not(onboard[T+1] == 1 and (nextTemp < t1 or nextTemp > t2)):
                    dp[T+1][nextTemp] = min(dp[T+1][nextTemp], dp[T][curTemp] + cost)
            
    
    answer = min(dp[time-1])
            
    
    return answer