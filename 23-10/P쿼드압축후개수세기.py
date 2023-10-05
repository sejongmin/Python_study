def count_function(x, y, now, arr):
    subsum = 0
    for i in range(x, x + now):
        for j in range(y, y + now):
            subsum += arr[i][j]
    if subsum == 0:
        return 0
    elif subsum == now ** 2:
        return 1
    else:
        return 2
            

def solution(arr):
    length = len(arr)
    visit = [[False] * length for _ in range(length)]
    answer = [0, 0]
    row, col = 0, 0
    now = length * 2
    
    while now > 1:
        now //= 2
        for i in range(row, length, now):
            for j in range(col, length, now):
                if visit[i][j] == False:
                    result = count_function(i, j, now, arr)
                    if result == 0:
                        answer[0] += 1
                        for x in range(i, i + now):
                            for y in range(j, j + now):
                                visit[x][y] = True
                    elif result == 1:
                        answer[1] += 1
                        for x in range(i, i + now):
                            for y in range(j, j + now):
                                visit[x][y] = True
                
    return answer