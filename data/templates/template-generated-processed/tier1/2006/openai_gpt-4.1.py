def solve():
    """Index: 2006.
    Returns: the membership cost in dollars in the sixth year.
    """
    # L1
    first_year_fee = 80 # he pays $80 in the first year
    yearly_increase = 10 # membership fee increases yearly by $10
    second_year_fee = first_year_fee + yearly_increase

    # L2
    third_year_fee = second_year_fee + yearly_increase

    # L3
    fourth_year_fee = third_year_fee + yearly_increase

    # L4
    fifth_year_fee = fourth_year_fee + yearly_increase

    # L5
    sixth_year_fee = fifth_year_fee + yearly_increase

    # FA
    answer = sixth_year_fee
    return answer