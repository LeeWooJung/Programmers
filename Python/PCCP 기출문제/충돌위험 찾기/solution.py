from collections import defaultdict

def getMove(prev, curr, t):
    
    prevR, prevC = prev
    currR, currC = curr
    
    path = []
    
    while prevR != currR:
        path.append((prevR, prevC, t))
        t += 1
        if prevR > currR:
            prevR -= 1
        else:
            prevR += 1
            
    while prevC != currC:
        
        path.append((currR, prevC, t))
        t += 1
        if prevC > currC:
            prevC -= 1
        else:
            prevC += 1
        
    return path, t
    

def solution(points, routes):
    answer = 0
    hashMap = defaultdict(lambda: 0)
    
    for route in routes:
        
        t = 0
        moveHistory = []
        
        for order in range(1, len(route)):
            
            prev = route[order - 1]
            current = route[order]
            
            prevPoint = points[prev - 1]
            curPoint = points[current - 1]
            
            history, t = getMove(prevPoint, curPoint, t)
            
            moveHistory.extend(history)
        
        moveHistory.append((curPoint[0], curPoint[1], t))
        
        for his in moveHistory:
            hashMap[his] += 1
            
        
    for value in hashMap.values():
        if value >= 2:
            answer += 1
        
            
    return answer