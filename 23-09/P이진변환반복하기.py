def len2bi(num):
    arr = []
    while num:
        arr.append(num % 2)
        num //= 2
    arr.reverse()
    
    return arr

def solution(s):
    answer = []
    
    cnt = 0
    zero_cnt = 0
    arr = list(map(int, list(s)))
    
    while 1:
        arr_sum, arr_len = sum(arr), len(arr)
        if arr_len == 1:
            break
        zero_cnt += arr_len - arr_sum
        cnt += 1
        
        arr = len2bi(arr_sum)
    
    answer = [cnt, zero_cnt]
    return answer