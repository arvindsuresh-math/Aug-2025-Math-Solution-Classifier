def solve():
    """Index: 583.
    Returns: the combined amount of water, in ounces, that leak from all three holes over a 2-hour time period.
    """
    # L1
    largest_rate = 3 # 3 ounces of water per minute (largest hole)
    medium_rate_divisor = 2 # one-half the rate of the largest hole
    medium_rate = largest_rate / medium_rate_divisor

    # L2
    small_rate_divisor = 3 # one-third the rate of the medium-sized hole
    small_rate = medium_rate / small_rate_divisor

    # L3
    combined_rate = largest_rate + medium_rate + small_rate

    # L4
    hours = 2 # 2-hour time period
    minutes_per_hour = 60 # WK
    total_minutes = hours * minutes_per_hour

    # L5
    total_leaked = total_minutes * combined_rate

    # FA
    answer = total_leaked
    return answer