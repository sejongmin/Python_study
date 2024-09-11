import sys
input = sys.stdin.readline

def solution(N, d, k, c, sushi):
    answer = 0
    sushi_dict = {}
    for i in range(k):
        sushi_dict[sushi[i]] = sushi_dict.get(sushi[i], 0) + 1
    for i in range(k, N + k):
        if sushi_dict[sushi[(i - k) % N]] == 1:
            sushi_dict.pop(sushi[(i - k) % N])
        else:
            sushi_dict[sushi[i - k]] -= 1
        sushi_dict[sushi[i % N]] = sushi_dict.get(sushi[i % N], 0) + 1

        now = len(sushi_dict)
        if now >= answer:
            answer = now
            if c not in sushi_dict.keys():
                answer += 1

    return answer

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
print(solution(N, d, k, c, sushi))