def solution(numbers):
    answer = set()
    
    def check(num):
        if num < 2:
            return False
        for i in range(2, int(num ** (1/2)) + 1):
            if num % i == 0:
                return False
        return True
    
    def back(visit, numbers, result):
        nonlocal answer
        if all(visit):
            if check(int(result)):
                answer.add(int(result))
            return
        
        for i in range(len(numbers)):
            if visit[i]:
                continue
            visit[i] = True
            back(visit, numbers, result + numbers[i])
            visit[i] = False
            
    numbers = list(numbers)
    candidates = []
    
    for i in range(1, 1 << len(numbers)):
        arr = []
        for j in range(len(numbers)):
            if i & (1 << j):
                arr.append(numbers[j])
        candidates.append(arr)
    
    for candidate in candidates:
        back([False] * len(candidate), candidate, "")

    return len(answer)
    