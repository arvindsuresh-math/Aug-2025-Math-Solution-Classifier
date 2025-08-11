def solve():
    """Index: 2196.
    Returns: the total amount paid after tax.
    """
    # L1
    earbuds_cost = 200 # earbuds that cost $200
    tax_rate_decimal = 0.15 # tax was 15%
    tax_amount = earbuds_cost * tax_rate_decimal

    # L2
    total_cost_after_tax = earbuds_cost + tax_amount

    # FA
    answer = total_cost_after_tax
    return answer