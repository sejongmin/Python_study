import sys
input = sys.stdin.readline

def solution(N, A, B, C, D):
    answer = 0 
    AB = []
    CD = []
    for i in range(N):
        for j in range(N):
            AB.append(A[i] + B[j])
            CD.append(C[i] + D[j])
    
    AB.sort()
    CD.sort()
    front = 0
    rear = len(AB) - 1

    while front < len(AB) and rear >= 0:
        if AB[front] + CD[rear] < 0:
            front += 1
        elif AB[front] + CD[rear] > 0:
            rear -= 1
        elif AB[front] + CD[rear] == 0:
            x, y = 1, 1
            for i in range(front + 1, len(AB)):
                if AB[front] == AB[i]:
                    x += 1
                else:
                    break
            for j in range(rear - 1, -1, -1):
                if CD[rear] == CD[j]:
                    y += 1
                else:
                    break

            front = front + x
            rear = rear - y
            answer += x * y
    
    print(answer)

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
solution(N, A, B, C, D)