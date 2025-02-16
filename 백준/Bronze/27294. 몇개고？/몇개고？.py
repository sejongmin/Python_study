S, M = map(int, input().split())
if 12 <= S <= 16:
    if M == 0:
        print(320)
    else:
        print(280)
else:
    print(280)