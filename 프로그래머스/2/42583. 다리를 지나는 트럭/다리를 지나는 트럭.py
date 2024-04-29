from collections import deque

def solution(bridge_length, weight, truck_weights):    
    bridge = deque([0] * bridge_length)
    N = len(truck_weights)
    second = 0
    current_weight = 0
    i = 0
    
    while i < N:
        second += 1
        if bridge[0]:
            current_weight -= bridge[0]
        if current_weight + truck_weights[i] <= weight:
            current_weight += truck_weights[i]
            bridge.append(truck_weights[i])
            i += 1
        else:
            bridge.append(0)
        bridge.popleft()
        
    return second + bridge_length
        