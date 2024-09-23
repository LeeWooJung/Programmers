def timeToSec(t):
    
    Min, Sec = map(int, t.split(":"))

    return Min*60 + Sec

def SecToTime(t):
    Min = t // 60
    Sec = t % 60
    
    return f'{Min:02}:{Sec:02}'

def isInOpening(op_start, op_end, t):
    
    if op_start <= t and t <= op_end:
        return op_end
    
    return t

def isInVideoLen(video_len, t):
    
    if t <= 0:
        return 0
    elif t >= video_len:
        return video_len
    
    return t
    
    
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len = timeToSec(video_len)
    pos = timeToSec(pos)
    op_start = timeToSec(op_start)
    op_end = timeToSec(op_end)
    
    for command in commands:
        pos = isInOpening(op_start, op_end, pos)
        if command == "prev":
            pos = isInVideoLen(video_len, pos - 10)
        elif command == "next":
            pos = isInVideoLen(video_len, pos + 10)
            
    pos = isInOpening(op_start, op_end, pos)
    
    
    return SecToTime(pos)