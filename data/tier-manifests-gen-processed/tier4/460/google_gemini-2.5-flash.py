def solve():
    """Index: 460.
    Returns: John's total earnings this year including his bonus.
    """
    # L1
    last_year_bonus_amount = 10000 # $10,000 bonus
    last_year_salary = 100000 # $100,000
    bonus_percentage = last_year_bonus_amount / last_year_salary

    # L2
    this_year_salary = 200000 # $200,000
    this_year_bonus_amount = this_year_salary * bonus_percentage

    # L3
    total_earnings_this_year = this_year_salary + this_year_bonus_amount

    # FA
    answer = total_earnings_this_year
    return answer