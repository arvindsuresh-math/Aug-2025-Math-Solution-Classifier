def solve():
    """Index: 4119.
    Returns: the total amount Grant made in his first three months.
    """
    # L1
    first_month_earnings = 350 # The first month he made 350$

    # L2
    more_than_double = 50 # 50$ more than double
    double_multiplier = 2 # double he made the first month
    second_month_earnings = more_than_double + double_multiplier * first_month_earnings

    # L3
    quadruple_multiplier = 4 # quadrupled the sum
    third_month_earnings = quadruple_multiplier * (first_month_earnings + second_month_earnings)

    # L4
    total_earnings = first_month_earnings + second_month_earnings + third_month_earnings

    # FA
    answer = total_earnings
    return answer