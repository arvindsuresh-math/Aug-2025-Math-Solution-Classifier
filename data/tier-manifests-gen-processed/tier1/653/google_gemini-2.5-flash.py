def solve():
    """Index: 653.
    Returns: Fred's weekly allowance.
    """
    # L1
    ended_with_dollars = 14 # ended with 14 dollars
    earned_from_car = 6 # earned 6 dollars
    before_washing_car = ended_with_dollars - earned_from_car

    # L2
    multiplier_for_half = 2 # half of his allowance (implied by 2*)
    weekly_allowance = multiplier_for_half * before_washing_car

    # FA
    answer = weekly_allowance
    return answer