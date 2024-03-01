def solution(elements):
    numbers = []
    arr = elements + elements
    
    for i in range(len(elements)):
        for j in range(0, len(elements) + i):
            numbers.append(sum(arr[j:j + i + 1]))
    
    return len(set(numbers))