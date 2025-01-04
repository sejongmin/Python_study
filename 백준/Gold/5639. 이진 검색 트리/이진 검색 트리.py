import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solution(arr: list) -> None:
    def post(left, right):
        if left > right - 1:
            return
        mid = right
        for i in range(left + 1, right):
            if arr[left] < arr[i]:
                mid = i
                break
        post(left + 1, mid)
        post(mid, right)
        print(arr[left])
    post(0, len(arr))

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
solution(arr)
