def solution(n, s, a, b, fares):
    answer = 10e9
    INF = 10e5
    arr = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        arr[i][i] = 0
        
    for n1, n2, fare in fares:
        if arr[n1-1][n2-1] > fare:
            arr[n1-1][n2-1] = fare
            arr[n2-1][n1-1] = fare
            
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[j][k] > arr[j][i] + arr[i][k]:
                    arr[j][k] = arr[j][i] + arr[i][k]
                
    for i in range(n):
        cost = arr[s - 1][i] + arr[i][a - 1] + arr[i][b - 1]
        answer = min(answer, cost)
    
    return answer