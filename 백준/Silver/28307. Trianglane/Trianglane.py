import sys
from collections import deque
input = sys.stdin.readline

def solution(C, trianglane):
    answer = 0
    for i in range(2):
        for j in range(0, C, 2):
            if trianglane[i][j]:
                answer += 3
                if trianglane[(i + 1) % 2][j]:
                    answer -= 1
                if j < C - 1 and trianglane[i][j + 1]:
                    answer -= 1
                if j > 0 and trianglane[i][j - 1]:
                    answer -= 1
    
    for i in range(2):
        for j in range(1, C, 2):
            if trianglane[i][j]:
                answer += 3
                if j < C - 1 and trianglane[i][j + 1]:
                    answer -= 1
                if j > 0 and trianglane[i][j - 1]:
                    answer -= 1
    
    print(answer)

C = int(input())
trianglane = [list(map(int, input().split())) for _ in range(2)]
solution(C, trianglane)