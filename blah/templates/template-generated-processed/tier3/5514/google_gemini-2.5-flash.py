def solve():
    """Index: 5514.
    Returns: the number of cherry sodas in the cooler.
    """
    # L3
    cherry_soda_coefficient = 1 # WK
    orange_pop_coefficient = 2 # twice as many cans of orange pop
    total_cans = 24 # 24 cans of cherry soda and orange pop
    combined_coefficient = cherry_soda_coefficient + orange_pop_coefficient

    # L4
    cherry_soda_cans = total_cans / combined_coefficient

    # FA
    answer = cherry_soda_cans
    return answer