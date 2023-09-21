def solution(users, emoticons):
    answer = [0, 0]
    
    ecnt = len(emoticons)
    sales = [10] * ecnt
    
    while 1:
        plus = 0
        amount = 0
        for sale, limit in users:
            user_sum = 0
            for i in range(ecnt):
                if sales[i] >= sale:
                    user_sum += emoticons[i] * (100 - sales[i]) // 100
            if user_sum >= limit:
                plus += 1
            else:
                amount += user_sum
                
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = amount
        elif answer[0] == plus:
            if answer[1] < amount:
                answer[1] = amount
                
        for i in range(ecnt):
            if sales[i] < 40:
                sales[i] += 10
                break
            elif sales[i] == 40:
                sales[i] = 10
                
        if sum(sales) == 10 * ecnt:
            break
        
    return answer