import sys
read = sys.stdin.readline

N = int(read())
if N == 1:
    N = 2

def prime(num):
    for i in range(2, int(num**(1/2) + 1)):
        if num % i == 0:
            return False
    return True

while True:
    if prime(N):
        if str(N) == str(N)[::-1]:
            print(N)
            break
    N += 1