s = list(input().strip())
check = int(s[-1])
num = 0
idx = 0

for i in range(12):
    if s[i] == '*':
        if i % 2 == 0:
            m = 1
        elif i % 2 == 1:
            m = 3
        continue
    if i % 2 == 0:
        num += int(s[i])
    elif i % 2 == 1:
        num += int(s[i]) * 3

for i in range(10):
    if ((num + m * i) + check) % 10== 0:
        print(i)
        break