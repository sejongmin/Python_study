import sys
input = sys.stdin.readline

def solution(S: str) -> None:
    answer = ""
    yonsei = "YONSEI"
    korea = "KOREA"
    y = 0
    k = 0
    for c in S:
        if c == yonsei[y]:
            y += 1
        if c == korea[k]:
            k += 1
        if y > 5:
            answer = yonsei
            break
        if k > 4:
            answer = korea
            break
    print(answer)

S = input().strip()
solution(S)