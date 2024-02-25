str = input()
answer = ""

for ch in list(str):
    if ord("A") <= ord(ch) <= ord("Z"):
        answer += chr(ord(ch) - ord("A") + ord("a"))
    elif ord("a") <= ord(ch) <= ord("z"):
        answer += chr(ord(ch) - ord("a") + ord("A"))
        
print(answer)