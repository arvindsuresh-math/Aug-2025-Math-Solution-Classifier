def solve():
    """Index: 1218.
    Returns: the total amount John paid for both pairs of shoes including tax.
    """
    # L1
    nikes_cost = 150 # $150 pair of Nikes
    boots_cost = 120 # $120 pair of work boots
    shoes_cost = nikes_cost + boots_cost

    # L2
    tax_rate = 0.1 # Tax is 10%
    tax_amount = shoes_cost * tax_rate

    # L3
    total_cost = shoes_cost + tax_amount

    # FA
    answer = total_cost
    return answer