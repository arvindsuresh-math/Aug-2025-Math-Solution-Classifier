def solve():
    """Index: 2564.
    Returns: the amount of money John made from the car.
    """
    # L1
    fix_cost = 20000 # cost $20,000 to fix
    discount_percent = 0.2 # 20% discount
    discount_amount = fix_cost * discount_percent

    # L2
    paid_amount = fix_cost - discount_amount

    # L3
    prize = 70000 # prize is $70,000
    keep_percent = 0.9 # keeps 90% of the money
    kept_amount = prize * keep_percent

    # L4
    profit = kept_amount - paid_amount

    # FA
    answer = profit
    return answer