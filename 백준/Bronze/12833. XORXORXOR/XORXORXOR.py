A, B, C = map(int, input().split())
answer = A
for i in range(C % 2):
    answer = answer ^ B
    
print(answer)