import sys
input = sys.stdin.readline

def solution(N, code, exchanges) -> None:
    info = {}
    for exchange in exchanges:
        name, bid, price = exchange.split()
        info[name] = (bid, float(price))
    
    print(code)
    for name, (bid, price) in info.items():
        answer = []
        for name_, (bid_, price_) in info.items():
            if name == name_:
                continue
            if bid == "buy" and bid_ == 'sell':
                if price >= price_:
                    answer.append(name_)
            elif bid == "sell" and bid_ == "buy":
                if price <= price_:
                    answer.append(name_)
        if answer:
            print(name+":", *answer)
        else:
            print(name+":", "NO-ONE")
        
    
while True:
    N, code = input().strip().split()
    if N == "0" and code == "END":
        break
    exchanges = []
    for _ in range(int(N)):
        info = input().strip()
        exchanges.append(info)
    solution(N, code, exchanges)
