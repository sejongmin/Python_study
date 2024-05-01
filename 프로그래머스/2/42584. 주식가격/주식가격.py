def solution(prices):
    answer = [0] * len(prices)
    stack = [(prices[-1], 0)]
    
    for i in range(len(prices) - 2, -1, -1):
        d = 1
        while stack and stack[-1][0] >= prices[i]:
            _, cnt = stack.pop()
            d += cnt
        stack.append((prices[i], d))
        answer[i] = d
        
    return answer