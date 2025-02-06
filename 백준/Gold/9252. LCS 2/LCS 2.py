import sys
input = sys.stdin.readline

def solution(s1: str, s2: str) -> None:
    s1 = [""] + list(s1)
    s2 = [""] + list(s2)
    lcs = [[""] * len(s2) for _ in range(len(s1))]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                lcs[i][j] = lcs[i - 1][j - 1] + s1[i]
            else:
                if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                    lcs[i][j] = lcs[i-1][j]
                else:
                    lcs[i][j] = lcs[i][j-1]

    print(len(lcs[-1][-1]))
    if lcs[-1][-1]:
        print(lcs[-1][-1])

s1 = input().strip()
s2 = input().strip()
solution(s1, s2)
