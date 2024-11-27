import sys
input = sys.stdin.readline

def solution(word):
    answer = ''
    symbols = ['*', '?', '/', '+', '!']
    letter = set()
    repeat = dict()

    for i in range(len(word)):
        c = word[i].lower()
        if c in letter:
            repeat[c] = repeat.get(c, len(repeat))
            answer += symbols[repeat[c]]
            continue
        letter.add(c)
        answer += word[i]

    print(answer)

while True:
    word = input().strip()
    if word == '#':
        break
    solution(word)
