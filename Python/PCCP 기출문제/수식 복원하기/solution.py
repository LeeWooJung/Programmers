def isEqual(leftValue, rightValue, sign, resValue):
    
    if sign == '-':
        if leftValue - rightValue == resValue:
            return True
        else:
            return False
    
    elif sign == '+':
        if leftValue + rightValue == resValue:
            return True
        else:
            return False

def getValue(value, notation):
    
    res = 0
    exp = 1
    
    while value > 0:
        
        rem = value % 10
        if rem >= notation:
            return -1
    
        res += rem * exp
        exp *= notation
        value //= 10
        
    return res
        

def findNotation(hints): # 힌트 뿐만 아니라, X 식으로도 활용해야 함

    result = set([2,3,4,5,6,7,8,9])
    notations = [2,3,4,5,6,7,8,9]
    
    for hint in hints:
        
        left = int(hint[0])
        sign = hint[1]
        right = int(hint[2])
        
        res = hint[4]
        if res != 'X':
            res = int(hint[4])
        
        correctNot = []
        
        for tempNotation in notations:
            leftValue = getValue(left, tempNotation)
            rightValue = getValue(right, tempNotation)
            if res != 'X':
                resValue = getValue(res, tempNotation)
            else:
                resValue = 0
            
            if leftValue != -1 and rightValue != -1 and resValue != -1:
                if res == 'X':
                    correctNot.append(tempNotation)
                elif isEqual(leftValue, rightValue, sign, resValue):
                    correctNot.append(tempNotation)
            
        result = result & set(correctNot)
        
    return list(result)

def toNotation(value, notation):
    
    res = ""
    
    if value == 0:
        return "0"
    
    while value > 0:
        
        res = str(value % notation) + res
        value //= notation
        
    return res
        

def getResult(toSolve, notations):
    
    result = "" + toSolve[0] + " " + toSolve[1] + " " + toSolve[2] + " = "
    
    left = int(toSolve[0])
    sign = toSolve[1]
    right = int(toSolve[2])
    
    res = set([])
    
    for notation in notations:
        
        leftValue = getValue(left, notation)
        rightValue = getValue(right, notation)
        
        if leftValue != -1 and rightValue != -1:
            
            if sign == '-':
                res.add(toNotation(leftValue - rightValue, notation))
            else:
                res.add(toNotation(leftValue + rightValue, notation))
                
    if len(res) >= 2:
        return result + "?"
    else:
        return result + list(res)[0]

def solution(expressions):
    answer = []
    toSolves = []
    hints = []
    
    for expression in expressions:
        
        splitted = expression.split(" ")
        if splitted[-1] == 'X':
            toSolves.append(splitted)
        
        hints.append(splitted)
            
    notations = findNotation(hints)
    
    for toSolve in toSolves:
        
        answer.append(getResult(toSolve, notations))
    
    return answer