import sys
input = sys.stdin.readline

def solution(S: str) -> None:
    res1 = ''
    res2 = ''
    cnt_1 = 0
    for i in range(len(S)):
        if S[i] == '1':
            cnt_1 += 1
    cnt_0 = len(S) - cnt_1
    cnt = 0
    for i in range(len(S)):
        if cnt == cnt_1 // 2 and S[i] == '1':
            res1 += '1'
        elif S[i] == '0':
            res1 += '0'
        elif S[i] == '1':
            cnt += 1
    cnt = 0
    for i in range(len(res1) - 1, -1, -1):
        if cnt == cnt_0 // 2 and res1[i] == '0':
            res2 += '0'
        elif res1[i] == '1':
            res2 += '1'
        elif res1[i] == '0':
            cnt += 1
    print(res2[::-1])

if __name__ == "__main__":
    S = input().strip()
    solution(S)
