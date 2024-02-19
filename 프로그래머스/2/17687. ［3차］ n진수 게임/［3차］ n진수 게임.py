def formation(number, n):
    arr = []
    while number:
        a = number % n
        if a < 10:
            arr.append(str(a))
        else:
            arr.append(chr(ord("A") + a - 10))
        number = number // n
    
    return arr[::-1]

def solution(n, t, m, p):
    answer = ''
    max_num = t * m
    numbers = ['0']
    for i in range(1, max_num + 1):
        numbers += formation(i, n)
        
    i = p - 1
    while len(answer) < t:
        answer += numbers[i]
        i += m

    return answer