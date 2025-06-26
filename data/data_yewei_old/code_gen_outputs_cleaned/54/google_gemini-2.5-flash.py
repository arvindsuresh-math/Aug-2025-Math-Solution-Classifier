def solve_54():
    total_earned = 28
    
    # L1: Calculate money spent on milkshake
    milkshake_cost = total_earned / 7
    
    # L2: Calculate money left after buying milkshake
    remaining_after_milkshake = total_earned - milkshake_cost
    
    # L3: Calculate money put in wallet (half of the rest)
    money_in_wallet = remaining_after_milkshake / 2
    
    # L4: Calculate money lost (money in wallet minus the $1 not shredded)
    money_lost = money_in_wallet - 1
    
    return int(money_lost)