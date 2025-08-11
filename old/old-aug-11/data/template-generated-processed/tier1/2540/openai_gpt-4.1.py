def solve():
    """Index: 2540.
    Returns: the amount by which the art piece will have increased in value in three years.
    """
    # L1
    purchase_price = 4000 # purchased an art piece for $4000
    multiplier_in_3_years = 3 # three times as much in another three years
    future_price = multiplier_in_3_years * purchase_price

    # L2
    increase = future_price - purchase_price

    # FA
    answer = increase
    return answer