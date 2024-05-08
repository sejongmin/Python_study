def solution(citations):
    citations.sort()
    n = len(citations)
    i = 0
    answer = 0
    
    for h in range(citations[-1] + 1):
        while citations[i] < h:
            i += 1
        if n - i >= h:
            answer = h
        
    return answer
