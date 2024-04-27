import sys
input = sys.stdin.readline

doc = input().rstrip()
s = input().rstrip()

def solution(doc, s):
    answer = 0
    m = len(doc)
    n = len(s)

    i = 0
    while i < m - n + 1:
        cnt = 0
        for j in range(n):
            if doc[i + j] != s[j]:
                break
            cnt += 1
        if cnt == n:
            answer += 1
            i += n - 1
        i += 1
    
    return answer

print(solution(doc, s))