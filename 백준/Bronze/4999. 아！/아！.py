import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
print("no" if len(a) < len(b) else "go")