def solution(bandage, health, attacks):
    damage = 0
    now = 0
    for time, attack in attacks:
        t = time - now
        if damage > 0:
            damage -= (t - 1) * bandage[1]
            damage -= (t - 1) // bandage[0] * bandage[2]
        damage = max(damage, 0)
        damage += attack
        if damage >= health:
            return -1
        now = time
    
    return health - damage
        