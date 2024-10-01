import sys
input = sys.stdin.readline

def solution(A, B, C):
    if B == 1:
        return A % C
    
    x = solution(A, B // 2, C)
    x = x * x % C
    if B % 2:
        x = x * A % C
    return x
        
A, B, C = map(int, input().split())
print(solution(A, B, C))