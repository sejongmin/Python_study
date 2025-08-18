import sys
input = sys.stdin.readline

def solution(N: int, K: int, arr: list) -> int:
    answer = 0
    nums = [0] * 100001
    front, rear = 0, 0
    nums[arr[front]] += 1
    while 1:
        front += 1
        if front >= N:
            break
        nums[arr[front]] += 1
        if nums[arr[front]] > K:
            while 1:
                nums[arr[rear]] -= 1
                if arr[rear] == arr[front]:
                    rear += 1
                    break
                rear += 1
        answer = max(answer, front - rear + 1)
    return answer

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(N, K, arr))
