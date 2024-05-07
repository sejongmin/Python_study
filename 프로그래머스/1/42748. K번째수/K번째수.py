def solution(array, commands):
    answer = []
    for i, j, k in commands:
        num = sorted(array[i - 1:j])[k - 1]
        answer.append(num)
    
    return answer