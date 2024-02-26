def solution(operations):
    arr = []
    for operation in operations:
        order, number = operation.split(" ")
        if order == "I":
            arr.append(int(number))
        elif order == "D":
            if arr:
                if number == "1":
                    arr.remove(max(arr))
                elif number == "-1":
                    arr.remove(min(arr))

    return [max(arr), min(arr)] if arr else [0, 0]