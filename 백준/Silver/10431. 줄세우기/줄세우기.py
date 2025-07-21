import sys
input = sys.stdin.readline

def solution(students: list) -> None:
    answer = 0
    order = [0] * 20
    order[0] = students[1]
    for i in range(2, 21):
        now = i - 2
        while now >= 0 and order[now] > students[i]:
            order[now + 1] = order[now]
            now -= 1
            answer += 1
        order[now + 1] = students[i]
    
    print(students[0], answer)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        students = list(map(int, input().split()))                
        solution(students)
