import sys
input = sys.stdin.readline

def solution(lengths: list) -> None:
    answer = "NIE"
    lengths.sort()
    for i in range(len(lengths) - 2):
        if lengths[i] + lengths[i + 1] > lengths[i + 2]:
            answer = f"{lengths[i]} {lengths[i + 1]} {lengths[i + 2]}"
            break
    print(answer)
    return

lengths = []
while length := int(input()):
    lengths.append(length)
solution(lengths)