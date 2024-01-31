def solution(n):
    answer = 0
    
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or 3 in list(map(int, str(answer))):
            answer += 1
    
    return answer