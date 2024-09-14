import sys
input = sys.stdin.readline

def solution(A, B):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    return A * B // gcd(A, B)
    
A, B = map(int, input().split())
print(solution(A, B))