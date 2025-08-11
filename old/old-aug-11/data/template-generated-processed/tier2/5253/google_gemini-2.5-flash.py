def solve():
    """Index: 5253.
    Returns: Cary's current wage.
    """
    # L1
    initial_wage = 10 # $10/hour
    raise_percent_num = 20 # 20% raise
    raise_percent_decimal = 0.2 # 20%
    raise_amount = initial_wage * raise_percent_decimal

    # L2
    wage_after_first_year = initial_wage + raise_amount

    # L3
    pay_cut_percent_num = 75 # cut to 75%
    pay_cut_percent_decimal = 0.75 # 75%
    final_wage = wage_after_first_year * pay_cut_percent_decimal

    # FA
    answer = final_wage
    return answer