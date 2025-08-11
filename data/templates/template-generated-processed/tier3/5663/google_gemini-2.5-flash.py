def solve():
    """Index: 5663.
    Returns: the amount of money David had left.
    """
    # L1
    rate_per_hour = 14 # The rate for mowing a lawn is $14 per hour
    hours_per_day = 2 # mowed for 2 hours a day
    earnings_per_day = rate_per_hour * hours_per_day

    # L2
    days_in_a_week = 7 # for a week
    total_earnings_week = earnings_per_day * days_in_a_week

    # L3
    shoe_cost_divisor = 2 # half of the money he made
    cost_of_shoes = total_earnings_week / shoe_cost_divisor

    # L4
    mom_money_divisor = 2 # half of the remaining money
    money_given_to_mom = cost_of_shoes / mom_money_divisor

    # L5
    total_spent_and_given = cost_of_shoes + money_given_to_mom

    # L6
    money_left = total_earnings_week - total_spent_and_given

    # FA
    answer = money_left
    return answer