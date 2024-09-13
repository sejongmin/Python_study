import sys
input = sys.stdin.readline

def solution(A_cnt, B_cnt, A, B):
    return len(A - B) + len(B - A)

A_cnt, B_cnt = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
print(solution(A_cnt, B_cnt, A, B))