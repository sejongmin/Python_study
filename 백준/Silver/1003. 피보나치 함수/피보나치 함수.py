import sys
input = sys.stdin.readline

def solution(T, N_list):
    for i in range(T):
        num = N_list[i]
        dp_zero = [1] + [0] * num
        dp_one = [0] * (num + 1)
        if num > 0:
            dp_one[1] = 1

        for n in range(2, num + 1):
            dp_zero[n] = dp_zero[n - 1] + dp_zero[n - 2]
            dp_one[n] = dp_one[n - 1] + dp_one[n - 2]

        print(dp_zero[num], dp_one[num])


T = int(input())
N_list = [int(input()) for _ in range(T)]
solution(T, N_list)