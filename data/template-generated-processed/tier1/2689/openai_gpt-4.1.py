def solve():
    """Index: 2689.
    Returns: the total number of years Devin has taught.
    """
    # L1
    calculus_years = 4 # Calculus for 4 years

    # L2
    algebra_multiplier = 2 # Algebra for twice as many years
    algebra_years = calculus_years * algebra_multiplier

    # L3
    statistics_multiplier = 5 # Statistics for 5 times as long as he taught Algebra
    statistics_years = algebra_years * statistics_multiplier

    # L4
    total_years = calculus_years + algebra_years + statistics_years

    # FA
    answer = total_years
    return answer