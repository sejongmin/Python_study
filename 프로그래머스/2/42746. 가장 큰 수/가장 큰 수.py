def solution(numbers):
    answer = ''.join(sorted(map(str, numbers), key=lambda x:(x * 4)[:4], reverse=True))
    return answer if answer[0] != "0" else "0"
    
