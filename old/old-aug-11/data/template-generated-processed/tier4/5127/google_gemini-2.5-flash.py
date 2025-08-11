def solve():
    """Index: 5127.
    Returns: the cost of their total bill after discount.
    """
    # L1
    curtis_steak_cost = 16.00 # Salisbury Steak that costs $16.00
    rob_steak_cost = 18.00 # Chicken Fried Steak at $18.00
    initial_total_cost = curtis_steak_cost + rob_steak_cost

    # L2
    discount_divisor = 2 # half off
    final_bill_cost = initial_total_cost / discount_divisor

    # FA
    answer = final_bill_cost
    return answer