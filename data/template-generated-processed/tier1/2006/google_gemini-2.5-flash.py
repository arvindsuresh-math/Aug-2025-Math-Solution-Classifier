def solve():
    """Index: 2006.
    Returns: the membership cost, in dollars, in the sixth year.
    """
    # L1
    initial_fee = 80 # pays $80 in the first year
    yearly_increase = 10 # increases yearly by $10
    fee_year_2 = initial_fee + yearly_increase

    # L2
    fee_year_3 = fee_year_2 + yearly_increase

    # L3
    fee_year_4 = fee_year_3 + yearly_increase

    # L4
    fee_year_5 = fee_year_4 + yearly_increase

    # L5
    fee_year_6 = fee_year_5 + yearly_increase

    # FA
    answer = fee_year_6
    return answer