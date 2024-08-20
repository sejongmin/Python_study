import sys
input = sys.stdin.readline

def solution(n, clothes):
    answer = 1
    clothes_dict = {}
    for _, k in clothes:
        clothes_dict[k] = clothes_dict.get(k, 0) + 1
    
    for v in clothes_dict.values():
        answer *= v + 1
    answer -= 1

    return answer

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = [input().strip().split() for _ in range(n)]
    print(solution(n, clothes))
