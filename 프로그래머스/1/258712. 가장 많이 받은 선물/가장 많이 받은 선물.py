def solution(friends, gifts):
    answer = 0
    num = len(friends)
    arr = [[0] * num for _ in range(num)]
    score = [0] * num
    counts = [0] * num
    
    for gift in gifts:
        g, r = gift.split(" ")
        gIndex = friends.index(g)
        rIndex = friends.index(r)
        
        arr[gIndex][rIndex] += 1
        
        score[gIndex] += 1
        score[rIndex] -= 1
        
    for i in range(num):
        for j in range(i + 1, num):
            if arr[i][j] > arr[j][i]:
                counts[i] += 1
            elif arr[i][j] < arr[j][i]:
                counts[j] += 1
            elif arr[i][j] == arr[j][i]:
                if score[i] > score[j]:
                    counts[i] += 1
                elif score[i] < score[j]:
                    counts[j] += 1
    
    answer = max(counts)
    
    return answer