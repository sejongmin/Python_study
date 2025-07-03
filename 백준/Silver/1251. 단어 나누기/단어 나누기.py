word = input()

N = len(word)
arr = []
for i in range(1, N - 1):
    for j in range(i + 1, N):
        arr.append(''.join([word[:i][::-1], word[i:j][::-1], word[j:][::-1]]))

arr.sort()
print(arr[0])
