def solution(n):
    arr = [[0] * _ for _ in range(1, n + 1)]
    num = 1
    maxNum = n * (n + 1) // 2
    startY = 0
    startX = 0
    
    while num <= maxNum:
        y = startY
        while y < n - startX:
            arr[y][startX] = num
            num += 1
            y += 1
        startX += 1
        
        x = startX
        while x <= n - startX and arr[n - startX][x] == 0:
            arr[n - startX][x] = num
            x += 1
            num += 1
        
        y = n - startX - 1
        while y > startY:
            arr[y][y - startX + 1] = num
            y -= 1
            num += 1
        startY += 2
        
    return sum(arr, [])
