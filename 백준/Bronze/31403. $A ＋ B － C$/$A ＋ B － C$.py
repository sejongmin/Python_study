import sys
input = sys.stdin.readline

def solution(A, B, C):
    print(int(A) + int(B) - C)
    print(int(A + B) - C)

A = input().strip()
B = input().strip()
C = int(input())
solution(A, B, C)