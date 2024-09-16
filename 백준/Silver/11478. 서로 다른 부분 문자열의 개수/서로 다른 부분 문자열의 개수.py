import sys
input = sys.stdin.readline

def solution(S):
    sub_str = set()
    len_str = len(S)
    for i in range(1, len_str + 1):
        for j in range(len_str - i + 1):
            sub_str.add(S[j:j+i])
    return len(sub_str)

S = input().strip()
print(solution(S))