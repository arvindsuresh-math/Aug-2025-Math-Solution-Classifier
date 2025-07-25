def solve():
    """Index: 3365.
    Returns: the total amount John paid.
    """
    # L1
    num_shirts = 3 # 3 dress shirts
    cost_per_shirt = 20 # $20 each
    cost_before_tax = num_shirts * cost_per_shirt

    # L2
    tax_rate_decimal = 0.1 # 10% tax
    tax_amount = cost_before_tax * tax_rate_decimal

    # L3
    total_paid = cost_before_tax + tax_amount

    # FA
    answer = total_paid
    return answer