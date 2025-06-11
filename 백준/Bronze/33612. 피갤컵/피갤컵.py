N = int(input())
y = 2024
m = 0

m += N * 7
y += m // 12
m = m % 12 + 1

print(str(y), str(m))