def solve():
    """Index: 2564.
    Returns: the money John made from the car.
    """
    # L1
    fix_cost = 20000 # It cost $20,000 to fix
    discount_percent = 0.2 # 20% discount
    discount_amount = fix_cost * discount_percent

    # L2
    paid_cost = fix_cost - discount_amount

    # L3
    prize_money = 70000 # The prize is $70,000
    kept_percent = 0.9 # only keeps 90% of the money
    money_kept = prize_money * kept_percent

    # L4
    money_made = money_kept - paid_cost

    # FA
    answer = money_made
    return answer