def solution(words):
    words.sort()
    N = len(words)
    arr = [0] * N
    now = 0
    
    for i in range(N - 1):
        l1 = len(words[i])
        l2 = len(words[i + 1])
        
        j = 0
        for j in range(min(l1, l2)):
            if words[i][j] != words[i + 1][j]:
                j -= 1
                break
        arr[i] = max(arr[i], min(j + 2, l1))
        arr[i + 1] = max(arr[i + 1], min(j + 2, l2))

    return sum(arr)