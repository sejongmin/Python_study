def solution(A,B):
    answer = 0
    n = len(A)
    sa = sorted(A)
    sb = sorted(B)
    
    for i in range(n):
        answer += sa[i] * sb[n - 1 - i]
        
    return answer