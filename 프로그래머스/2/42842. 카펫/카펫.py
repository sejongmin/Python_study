def solution(brown, yellow):
    answer = []
    block = brown + yellow
    candidate = []
    
    for i in range(3, int(block ** (1 / 2)) + 1):
        if block % i == 0:
            candidate.append((block // i, i))
        
    for w, h in candidate:
        if 2 * w + 2 * h - 4 == brown:
            return [w, h]