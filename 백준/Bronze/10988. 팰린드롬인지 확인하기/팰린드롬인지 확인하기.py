import sys
input = sys.stdin.readline

s = input().strip()

left, right = 0, len(s) - 1
answer = 1

while left < right:
    if s[left] != s[right]:
        answer = 0
        break
    left += 1
    right -= 1

print(answer)