def solution(clothes):
    answer = 1
    dict = {}
    for c, t in clothes:
        dict[t] = dict.get(t, 0) + 1
    
    for v in dict.values():
        answer *= v + 1
    
    return answer - 1
    