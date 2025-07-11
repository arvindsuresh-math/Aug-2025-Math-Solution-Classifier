def solve():
    """Index: 583.
    Returns: the combined amount of water, in ounces, that leak from all three holes.
    """
    # L1
    largest_hole_leak_rate = 3 # 3 ounces of water per minute
    medium_hole_rate_divisor = 2 # one-half the rate
    medium_hole_leak_rate = largest_hole_leak_rate / medium_hole_rate_divisor

    # L2
    small_hole_rate_divisor = 3 # one-third the rate
    small_hole_leak_rate = medium_hole_leak_rate / small_hole_rate_divisor

    # L3
    combined_leak_rate = largest_hole_leak_rate + medium_hole_leak_rate + small_hole_leak_rate

    # L4
    time_hours = 2 # 2-hour time period
    minutes_per_hour = 60 # WK
    total_minutes = time_hours * minutes_per_hour

    # L5
    total_water_leaked = total_minutes * combined_leak_rate

    # FA
    answer = total_water_leaked
    return answer