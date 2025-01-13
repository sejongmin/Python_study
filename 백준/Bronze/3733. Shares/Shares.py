result = []

while True:
    try:
        n, s = map(int, input().split())
        result.append(s // (n+1))
    except:
        for x in result:
            print(x)
        break