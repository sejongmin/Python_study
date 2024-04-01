def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    
    while B:
        if A[0] < B[0]:
            A.pop(0)
            B.pop(0)
            answer += 1
        else:
            B.pop(0)
            
    return answer