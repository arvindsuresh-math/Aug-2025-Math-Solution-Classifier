def solve():
    """Index: 7135.
    Returns: the amount Jan paid for the roses.
    """
    # L1
    num_dozens = 5 # 5 dozen roses
    roses_per_dozen = 12 # WK
    total_roses = num_dozens * roses_per_dozen

    # L2
    cost_per_rose = 6 # Each rose cost $6
    base_cost = cost_per_rose * total_roses

    # L3
    payment_percentage = 0.8 # pay 80%
    final_payment = base_cost * payment_percentage

    # FA
    answer = final_payment
    return answer