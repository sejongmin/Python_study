import sys
input = sys.stdin.readline

while '#' not in (info := input().strip().split())[0]:
    if int(info[1]) > 17 or int(info[2]) >= 80:
        print(info[0], 'Senior')
    else:
        print(info[0], 'Junior')