def solution(word):
    words = ["A", "E", "I", "O", "U"]
    gap = [781, 156, 31, 6, 1]
    answer = 0
    for i in range(len(word)):
        answer += gap[i] * words.index(word[i]) + 1
    return answer