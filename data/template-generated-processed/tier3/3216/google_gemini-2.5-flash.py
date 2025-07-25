def solve():
    """Index: 3216.
    Returns: the total amount Kyle would have to spend on roses.
    """
    # L1
    roses_last_year = 12 # a dozen roses
    half_divisor = 2 # half the number of roses
    roses_this_year = roses_last_year / half_divisor

    # L2
    twice_multiplier = 2 # twice as many roses as last year
    desired_roses = roses_last_year * twice_multiplier

    # L3
    roses_needed = desired_roses - roses_this_year

    # L4
    cost_per_rose = 3 # one rose for $3
    total_cost = roses_needed * cost_per_rose

    # FA
    answer = total_cost
    return answer