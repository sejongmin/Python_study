import sys
input = sys.stdin.readline

def solution(N:int, milks: list) -> None:
    answer = 0
    for milk in milks:
        if milk == answer % 3:
            answer += 1
    
    print(answer)

N = int(input())
milks = list(map(int, input().split()))
solution(N, milks)