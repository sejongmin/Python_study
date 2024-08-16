import sys
input = sys.stdin.readline

def solution(A, B, C):
    print(int(A) + int(B) - int(C))
    print(int(A + B) - int(C))

A = input().strip()
B = input().strip()
C = input().strip()
solution(A, B, C)