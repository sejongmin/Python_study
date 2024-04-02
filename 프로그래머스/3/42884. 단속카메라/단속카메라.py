def solution(routes):
    answer = 0
    high = -30000
    low = 30000
    
    routes.sort(key=lambda x:x[0])

    for route in routes:
        if high >= route[0]:
            low = max(low, route[0])
            high = min(high, route[1])
        else:
            answer += 1
            low = route[0]
            high = route[1]
            
    return answer