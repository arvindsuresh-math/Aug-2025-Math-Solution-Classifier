def solve():
    """Index: 653.
    Returns: Fred's weekly allowance.
    """
    # L1
    final_amount = 14 # ended with 14 dollars
    car_wash_earnings = 6 # earned 6 dollars
    before_car_wash = final_amount - car_wash_earnings

    # L2
    multiplier_for_half = 2 # spent half his allowance
    allowance = multiplier_for_half * before_car_wash

    # FA
    answer = allowance
    return answer