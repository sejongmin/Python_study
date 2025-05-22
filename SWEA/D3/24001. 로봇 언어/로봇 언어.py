def solution(command):
    length = len(command)
    answer = 0
    now = 0
    q = 0
    for i in range(length):
        if command[i] == '?':
            q += 1
        elif command[i] == 'L':
            now -= 1
        elif command[i] == 'R':
            now += 1
        answer = max(answer, abs(now - q), abs(now + q))
    return answer

T = int(input())

for i in range(1, T + 1):
    command = input().strip()
    print(solution(command))