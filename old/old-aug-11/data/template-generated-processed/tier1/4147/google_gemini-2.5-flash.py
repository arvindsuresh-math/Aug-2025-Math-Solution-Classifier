def solve():
    """Index: 4147.
    Returns: the total number of stamps in Tom's collection.
    """
    # L1
    mike_gift_stamps = 17 # If Mike has given Tom 17 stamps
    multiplier_twice = 2 # Twice the number
    twice_mike_gift = mike_gift_stamps * multiplier_twice

    # L2
    harry_more_than_twice_mike = 10 # 10 more stamps than twice Mike’s gift
    harry_gift_stamps = harry_more_than_twice_mike + twice_mike_gift

    # L3
    total_gifts = harry_gift_stamps + mike_gift_stamps

    # L4
    tom_initial_stamps = 3000 # Tom, an avid stamp collector, has 3,000 stamps in his collection
    tom_total_stamps = tom_initial_stamps + total_gifts

    # FA
    answer = tom_total_stamps
    return answer