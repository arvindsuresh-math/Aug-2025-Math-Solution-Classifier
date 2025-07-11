def solve():
    """Index: 568.
    Returns: the total amount John paid for raising the child and university tuition.
    """
    # L1
    first_period_years = 8 # first 8 years
    first_period_cost_per_year = 10000 # $10,000 a year for the first 8 years
    first_period_total = first_period_years * first_period_cost_per_year

    # L2
    total_years = 18 # until the child is 18
    next_period_years = total_years - first_period_years

    # L3
    next_period_cost_per_year = first_period_cost_per_year * 2

    # L4
    next_period_total = next_period_cost_per_year * next_period_years

    # L5
    total_cost_before_tuition = next_period_total + first_period_total

    # L6
    tuition_cost = 250000 # University tuition then costs $250,000
    total_cost_with_tuition = tuition_cost + total_cost_before_tuition

    # L7
    john_share_divisor = 2 # John pays for half the cost
    answer = total_cost_with_tuition / john_share_divisor
    return answer