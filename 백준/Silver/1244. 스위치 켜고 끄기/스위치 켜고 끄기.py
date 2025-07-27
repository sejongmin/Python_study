import sys
input = sys.stdin.readline

def solution(N: int, switch: list, M: int, students: list) -> None:
    for gender, number in students:
        if gender == 1:
            for i in range(number, N + 1, number):
                switch[i] = 0 if switch[i] else 1
        elif gender == 2:
            switch[number] = 0 if switch[number] else 1
            for i in range(1, min(N - number + 1, number)):
                if switch[number + i] != switch[number - i]:
                    break
                switch[number + i] = 0 if switch[number + i] else 1
                switch[number - i] = 0 if switch[number - i] else 1
    for i in range(1, N + 1):
        print(switch[i], end=' ')
        if i % 20 == 0:
            print()

if __name__ == "__main__":
    N = int(input())
    switch = [0] + list(map(int, input().split()))
    M = int(input())
    students = [list(map(int, input().split())) for _ in range(M)]
    solution(N, switch, M, students)
