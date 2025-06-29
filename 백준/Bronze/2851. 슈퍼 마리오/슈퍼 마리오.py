import sys
input = sys.stdin.readline

TARGET = 100
MUSHROOM_COUNT = 10

def solution(mushrooms: list) -> int:
    answer = 0
    res = 0
    
    for mush in mushrooms:
        res += mush
        if res <= TARGET:
            answer = res
        elif res > TARGET:
            if abs(TARGET - answer) >= abs(TARGET - res):
                answer = res
            break
        
    return answer

mushrooms = [int(input()) for _ in range(MUSHROOM_COUNT)]
print(solution(mushrooms))
