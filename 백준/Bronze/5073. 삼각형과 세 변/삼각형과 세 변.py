import sys
input = sys.stdin.readline

def solution(tri):
    tri.sort()
    if tri[0] + tri[1] <= tri[2]:
        print("Invalid")
        return
    
    temp = len(set(tri))
    
    if temp == 1:
        print("Equilateral")
    elif temp == 2:
        print("Isosceles")
    elif temp == 3:
        print("Scalene")

while (tri := list(map(int, input().split()))) != [0, 0, 0]:
    solution(tri)
