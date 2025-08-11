def solve():
    """Index: 6324.
    Returns: the number of cans recycled.
    """
    # L1
    bottle_deposit_per_bottle = 0.10 # 10 cents per bottle
    num_bottles = 80 # 80 bottles
    earnings_from_bottles = bottle_deposit_per_bottle * num_bottles

    # L2
    total_earnings = 15.00 # made $15
    earnings_from_cans = total_earnings - earnings_from_bottles

    # L3
    can_deposit_per_can = 0.05 # 5 cents per can
    num_cans = earnings_from_cans / can_deposit_per_can

    # FA
    answer = num_cans
    return answer