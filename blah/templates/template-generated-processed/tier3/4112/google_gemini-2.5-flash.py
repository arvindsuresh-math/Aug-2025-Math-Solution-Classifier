def solve():
    """Index: 4112.
    Returns: the total dollars the farmer will make from the pig's bacon.
    """
    # L1
    average_bacon_pounds = 20 # 20 pounds of bacon on average from a pig
    size_divisor = 2 # half the size
    runt_bacon_pounds = average_bacon_pounds / size_divisor

    # L2
    price_per_pound = 6 # sells each pound for $6
    total_earnings = runt_bacon_pounds * price_per_pound

    # FA
    answer = total_earnings
    return answer