import sys
input = sys.stdin.readline

def solution(s: str) -> bool:
    vowel = {'a', 'e', 'i', 'o', 'u'}
    before = s[0]
    t_acc = 1 if before in vowel else 0
    v_acc = 1 if before in vowel else 0
    c_acc = 0 if before in vowel else 1
    for i in range(1, len(s)):
        if before == s[i]:
            if before != 'e' and before != 'o':
                return False
        if s[i] in vowel:
            t_acc += 1
            c_acc = 0
            v_acc += 1
            if v_acc == 3:
                return False
        elif s[i] not in vowel:
            v_acc = 0
            c_acc += 1
            if c_acc == 3:
                return False
        before = s[i]

    return True if t_acc > 0 else False

if __name__ == "__main__":
    while (s := input().strip()) != 'end':
        if solution(s):
            print(f'<{s}> is acceptable.')
            continue
        print(f'<{s}> is not acceptable.')
