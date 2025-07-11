def solve():
    """Index: 288.
    Returns: the total amount John paid in the first year for gym membership.
    """
    # L1
    cheap_monthly = 10 # The cheap one costs $10 a month
    months_in_year = 12 # WK
    cheap_yearly_fees = cheap_monthly * months_in_year

    # L2
    cheap_signup = 50 # sign-up fee of $50
    cheap_total = cheap_yearly_fees + cheap_signup

    # L3
    expensive_multiplier = 3 # 3 times more expensive
    expensive_monthly = expensive_multiplier * cheap_monthly

    # L4
    expensive_signup_months = 4 # sign-up fee of 4 months membership
    expensive_signup = expensive_monthly * expensive_signup_months

    # L5
    expensive_yearly_fees = expensive_monthly * months_in_year

    # L6
    expensive_total = expensive_yearly_fees + expensive_signup

    # L7
    total_cost = expensive_total + cheap_total

    # FA
    answer = total_cost
    return answer