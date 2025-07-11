def solve():
    """Index: 2196.
    Returns: the total amount John paid after tax for the earbuds.
    """
    # L1
    earbuds_cost = 200 # cost $200
    tax_rate = 0.15 # tax was 15%
    tax_amount = earbuds_cost * tax_rate

    # L2
    total_paid = earbuds_cost + tax_amount

    # FA
    answer = total_paid
    return answer