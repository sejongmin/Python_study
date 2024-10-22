import sys
input = sys.stdin.readline

def solution(s, bomb):
    result = []
    for c in s:
        result.append(c)
        if ''.join(result[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                result.pop()

    print(''.join(result) if result else "FRULA")

s = input().strip()
bomb = input().strip()
solution(s, bomb)