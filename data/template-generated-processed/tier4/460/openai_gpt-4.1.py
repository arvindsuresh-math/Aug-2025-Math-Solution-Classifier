def solve():
    """Index: 460.
    Returns: John's total pay this year including his bonus.
    """
    # L1
    last_year_pay = 100000 # Last year he made $100,000
    last_year_bonus = 10000 # got a $10,000 bonus
    bonus_percent = last_year_bonus / last_year_pay

    # L2
    this_year_pay = 200000 # This year he makes $200,000
    this_year_bonus = this_year_pay * bonus_percent

    # L3
    total_this_year = this_year_pay + this_year_bonus

    # FA
    answer = total_this_year
    return answer