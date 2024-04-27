def solution(my_string):
    l = list(my_string)
    s = set(my_string)
    arr = []
    
    for i in l:
        if i in s:
            arr.append(i)
            s.remove(i)
        
    return ''.join(arr)
    