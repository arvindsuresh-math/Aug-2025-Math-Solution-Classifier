def solve():
    """Index: 2449.
    Returns: the amount of change Yanna got back from $100 after her purchases.
    """
    # L1
    num_shirts = 10 # ten shirts
    price_per_shirt = 5 # $5 each
    shirts_total = num_shirts * price_per_shirt

    # L2
    num_sandals = 3 # three pairs of sandals
    price_per_sandal = 3 # $3 each
    sandals_total = num_sandals * price_per_sandal

    # L3
    total_spent = shirts_total + sandals_total

    # L4
    bill_given = 100 # one hundred dollar bill
    change = bill_given - total_spent

    # FA
    answer = change
    return answer