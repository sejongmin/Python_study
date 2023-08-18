import sys
read = sys.stdin.readline

def OneTwoThree (n) :
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return OneTwoThree(n - 1) + OneTwoThree(n - 2) + OneTwoThree(n - 3)

T = int(read().strip())

for _ in range(T):
    n = int(read().strip())
    print(OneTwoThree(n))