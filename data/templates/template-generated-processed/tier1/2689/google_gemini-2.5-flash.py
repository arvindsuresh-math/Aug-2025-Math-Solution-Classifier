def solve():
    """Index: 2689.
    Returns: the total number of years Devin has taught.
    """
    # L1
    calculus_years = 4 # taught Calculus for 4 years
    calculus_years_taught = calculus_years

    # L2
    algebra_multiplier = 2 # twice as many years
    algebra_years_taught = calculus_years_taught * algebra_multiplier

    # L3
    statistics_multiplier = 5 # 5 times as long as he taught Algebra
    statistics_years_taught = algebra_years_taught * statistics_multiplier

    # L4
    total_years_taught = calculus_years_taught + algebra_years_taught + statistics_years_taught

    # FA
    answer = total_years_taught
    return answer