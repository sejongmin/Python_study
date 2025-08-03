import sys
input = sys.stdin.readline

def solution(num: str) -> int:
    result = 1
    index = 0
    while index < len(num):
        for k in str(result):
            if k in num[index]:
                index += 1
                if index == len(num):
                    break
        result += 1

    return result - 1

if __name__ == "__main__":
    num = input().strip()
    print(solution(num))

