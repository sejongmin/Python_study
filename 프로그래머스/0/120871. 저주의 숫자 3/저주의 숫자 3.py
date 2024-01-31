def solution(n):
    answer = 0
    i = 0
    while True:
        if i == n:
            break
            
        i += 1
        answer += 1
        while answer % 3 == 0 or 3 in list(map(int, str(answer))):
            answer += 1
    
    return answer