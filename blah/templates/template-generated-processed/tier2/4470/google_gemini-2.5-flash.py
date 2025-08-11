def solve():
    """Index: 4470.
    Returns: the amount Tim paid for the cabinet.
    """
    # L1
    cabinet_cost = 1200 # Tim buys a cabinet for $1200
    discount_rate = 0.15 # gets a 15% discount
    discount_amount = cabinet_cost * discount_rate

    # L2
    amount_paid = cabinet_cost - discount_amount

    # FA
    answer = amount_paid
    return answer