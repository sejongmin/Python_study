def DFS(arr, left, right, depth):
    if left == right:
        return True
    center = left + (right - left) // 2
    
    if DFS(arr, left, center - 1, depth + 1) and DFS(arr, center + 1, right, depth + 1):
        if arr[center - (center - left + 1) // 2] or arr[center + (right - center + 1) // 2]:
            if arr[center] == 0:
                return False
            else:
                return True
        else:
            return True
    else:
        return False

def solution(numbers):
    answer = []
    
    for number in numbers:
        i = 1
        while 1:
            if number > 2 ** i - 1:
                i += (i + 1)
            else:
                break
                
        number_bi = []
        while number:
            number_bi.append(number % 2)
            number //= 2
        for _ in range((i - len(number_bi))):
            number_bi.append(0)
        number_bi.reverse()
        
        if DFS(number_bi, 0, i - 1, 0):
            answer.append(1)
        else:
            answer.append(0)
    
    
    return answer