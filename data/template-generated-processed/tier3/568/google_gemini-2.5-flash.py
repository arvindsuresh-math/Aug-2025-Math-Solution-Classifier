def solve():
    """Index: 568.
    Returns: the total cost John paid for raising the child and tuition.
    """
    # L1
    first_period_years = 8 # for the first 8 years
    cost_per_year_first_period = 10000 # $10,000 a year
    cost_first_period = first_period_years * cost_per_year_first_period

    # L2
    child_age_end = 18 # until the child is 18
    next_period_years = child_age_end - first_period_years

    # L3
    multiplier_for_second_period_cost = 2 # twice that much
    cost_per_year_second_period = cost_per_year_first_period * multiplier_for_second_period_cost

    # L4
    cost_second_period = cost_per_year_second_period * next_period_years

    # L5
    total_cost_before_tuition = cost_second_period + cost_first_period

    # L6
    university_tuition_cost = 250000 # University tuition then costs $250,000
    total_cost_with_tuition = university_tuition_cost + total_cost_before_tuition

    # L7
    johns_share_divisor = 2 # half the cost
    johns_total_payment = total_cost_with_tuition / johns_share_divisor

    # FA
    answer = johns_total_payment
    return answer