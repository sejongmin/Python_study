def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = answer * arr[i] // gcd(answer, arr[i])
    
    return answer