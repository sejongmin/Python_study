def solution(record):
    answer = []
    logs = []
    chat = set([])
    chat_name = {}
    
    for r in record:
        arr = r.split(" ")
        
        if "Change" == arr[0]:
            chat_name[arr[1]] = arr[2]
        else:
            logs.append([arr[0], arr[1]])
            if "Enter" == arr[0]:
                chat.add(arr[1])
                chat_name[arr[1]] = arr[2]
            elif "Leave" == arr[0]:
                chat.remove(arr[1])
        
    for log in logs:
        message = chat_name[log[1]] + "님이 "
        if log[0] == "Enter":
            message += "들어왔습니다."
        elif log[0] == "Leave":
            message += "나갔습니다."
        answer.append(message)
        
    return answer
            