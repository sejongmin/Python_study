import sys
input = sys.stdin.readline

def solution(input_list):
    num = 0

    for i in range(3):
        if '0' <= input_list[i][0] <= '9':
            num = int(input_list[i])
        num += 1

    if num % 3 and num % 5:
        return num
    elif num % 3:
        return "Buzz"
    elif num % 5:
        return "Fizz"
    else:
        return "FizzBuzz"

input_list = [input().strip() for _ in range(3)]
print(solution(input_list))