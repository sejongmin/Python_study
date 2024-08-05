def solution(data, ext, val_ext, sort_by):
    arr = []
    h = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    for i in range(len(data)):
        if data[i][h[ext]] < val_ext:
            arr.append(data[i])
    
    answer = sorted(arr, key=lambda x : x[h[sort_by]])
    return answer