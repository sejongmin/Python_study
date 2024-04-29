import sys
input = sys.stdin.readline

N = int(input())

answer = N // 5
answer += N // 25
answer += N // 125

print(answer)