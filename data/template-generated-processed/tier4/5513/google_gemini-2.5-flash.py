def solve():
    """Index: 5513.
    Returns: the difference in money between scheme A and scheme B after a year.
    """
    # L1
    scheme_a_yield_percent_num = 30 # 30% of the capital
    percent_divisor = 100 # WK
    scheme_a_capital = 300 # invested $300 in scheme A
    scheme_a_yield = (scheme_a_yield_percent_num / percent_divisor) * scheme_a_capital

    # L2
    total_scheme_a = scheme_a_yield + scheme_a_capital

    # L3
    scheme_b_yield_percent_num = 50 # 50% of the capital
    percent_factor = 0.01 # WK
    scheme_b_capital = 200 # invested $200 in B
    scheme_b_yield = scheme_b_yield_percent_num * percent_factor * scheme_b_capital

    # L4
    total_scheme_b = scheme_b_yield + scheme_b_capital

    # L5
    difference_a_b = total_scheme_a - total_scheme_b

    # FA
    answer = difference_a_b
    return answer