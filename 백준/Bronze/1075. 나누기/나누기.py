n = int(input())
m = int(input())

n = n // 100
answer = n * 100

while answer % m != 0:
    answer += 1
print(str(answer)[-2:])
