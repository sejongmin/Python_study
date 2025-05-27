import sys
input = sys.stdin.readline 

def solution(A, B):
    answer = 50
    gap = len(B) - len(A)

    for i in range(gap + 1):
        cnt = 0
        for j in range(len(A)):
            if A[j] != B[i + j]:
                cnt += 1
        if answer > cnt:
            answer = cnt
    
    return answer

A, B = input().strip().split()
print(solution(A, B))