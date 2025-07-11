def solve():
    """Index: 288.
    Returns: the total cost paid in the first year for gym membership.
    """
    # L1
    cheap_gym_monthly_cost = 10 # $10 a month
    months_in_year = 12 # WK
    cheap_gym_yearly_monthly_fees = cheap_gym_monthly_cost * months_in_year

    # L2
    cheap_gym_signup_fee = 50 # sign-up fee of $50
    total_cost_cheap_gym = cheap_gym_yearly_monthly_fees + cheap_gym_signup_fee

    # L3
    expensive_gym_cost_multiplier = 3 # 3 times more expensive
    expensive_gym_monthly_cost = expensive_gym_cost_multiplier * cheap_gym_monthly_cost

    # L4
    expensive_gym_signup_fee_months = 4 # sign-up fee of 4 months membership
    expensive_gym_signup_fee = expensive_gym_monthly_cost * expensive_gym_signup_fee_months

    # L5
    expensive_gym_yearly_monthly_fees = expensive_gym_monthly_cost * months_in_year

    # L6
    total_cost_expensive_gym = expensive_gym_yearly_monthly_fees + expensive_gym_signup_fee

    # L7
    total_gym_membership_cost = total_cost_expensive_gym + total_cost_cheap_gym

    # FA
    answer = total_gym_membership_cost
    return answer