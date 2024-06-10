def solution(numbers, target):
    answer = 0
    def dfs(result, depth):
        nonlocal answer, numbers, target
        if depth == len(numbers):
            if result == target:
                answer += 1
            return
        dfs(result + numbers[depth], depth + 1)
        dfs(result - numbers[depth], depth + 1)
        
    dfs(0, 0)
    return answer