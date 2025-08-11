def solve():
    """Index: 1218.
    Returns: the total amount John paid for everything.
    """
    # L1
    nike_cost = 150 # $150 pair of Nikes
    boots_cost = 120 # $120 pair of work boots
    shoes_total_cost = nike_cost + boots_cost

    # L2
    tax_rate_decimal = 0.1 # Tax is 10%
    tax_amount = shoes_total_cost * tax_rate_decimal

    # L3
    total_cost = shoes_total_cost + tax_amount

    # FA
    answer = total_cost
    return answer