import sys
input = sys.stdin.readline

while True:
    a = input().strip()
    if a == '#':
        break
    answer = 0
    for i in a:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            answer += 1
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            answer += 1
    print(answer)