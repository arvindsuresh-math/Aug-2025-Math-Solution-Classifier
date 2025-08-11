def solve():
    """Index: 6112.
    Returns: the total amount Tim paid for the manicure.
    """
    # L1
    manicure_cost = 30 # manicure cost $30
    tip_rate_decimal = 0.3 # tips the beautician 30%
    tip_amount = manicure_cost * tip_rate_decimal

    # L2
    total_paid = manicure_cost + tip_amount

    # FA
    answer = total_paid
    return answer