def solution(number, k):
    arr = [number[0]]
    cnt = 0
    idx = len(number)
    for i in range(1, len(number)):
        while arr and cnt < k and number[i] > arr[-1]:
            arr.pop()
            cnt += 1
        arr.append(number[i])
        if cnt == k:
            idx = i
            break

    while cnt < k:
        arr.pop()
        cnt += 1
        idx += 1
    return ''.join(arr) + number[idx + 1:]