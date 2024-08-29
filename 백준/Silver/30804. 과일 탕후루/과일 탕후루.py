import sys
input = sys.stdin.readline

def solution(N, fruits):
    answer = 0
    front, rear = 0, 0
    f_cnt = {i:0 for i in range(1, 10)}
    f_type = set()
    
    while front < N:
        while front < N and len(f_type) < 3:
            fruit = fruits[front]
            f_cnt[fruit] += 1
            f_type.add(fruit)
            front += 1
        temp = 0 if len(f_type) < 3 else 1
        answer = max(answer, front - rear - temp)
        while rear < front and len(f_type) > 2:
            fruit = fruits[rear]
            f_cnt[fruit] -= 1
            if f_cnt[fruit] == 0:
                f_type.remove(fruit)
            rear += 1

    return answer

N = int(input())
fruits = list(map(int, input().split()))
print(solution(N, fruits))