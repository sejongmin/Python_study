import sys
input = sys.stdin.readline

def solution(n: int, pillars: list) -> int:
    answer = 0
    warehouse = [0] * 1001
    max_height = 0
    for l, h in pillars:
        warehouse[l] = h
        if max_height < h:
            max_height = h
    
    i = 0
    now = 0
    while 1:
        if max_height == warehouse[i]:
            break
        if now < warehouse[i]:
            now = warehouse[i]
        answer += now
        i += 1
    front = i
    
    i = 1000
    now = 0
    while 1:
        if max_height == warehouse[i]:
            break
        if now < warehouse[i]:
            now = warehouse[i]
        answer += now
        i -= 1
    rear = i

    answer += max_height * (rear - front + 1)
    return answer

if __name__ == "__main__":
    n = int(input())
    pillars = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, pillars))
