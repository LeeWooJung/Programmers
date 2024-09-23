def getTime(diffs, times, level):
    
    totTime = times[0]
    
    for i in range(1, len(diffs)):
        
        time_prev = times[i-1]
        time_cur = times[i]
        
        diff = diffs[i]
        
        if level >= diff:
            totTime += time_cur
        else:
            totTime += (time_prev + time_cur) * (diff - level) + time_cur
            
    return totTime
    

def solution(diffs, times, limit):
    answer = 0
    
    left = min(diffs)
    right = max(diffs)
    
    while left < right:
        
        mid = (left + right) // 2
        
        totTime = getTime(diffs, times, mid)
        
        if totTime > limit: # lower bound
            left = mid + 1
        else:
            right = mid
    
    return left