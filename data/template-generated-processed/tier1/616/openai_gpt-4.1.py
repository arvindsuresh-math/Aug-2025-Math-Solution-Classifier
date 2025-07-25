def solve():
    """Index: 616.
    Returns: the total number of balloons Kris and her brother blew up in 30 minutes.
    """
    # L1
    kris_balloons_per_min = 2 # Kris can blow up a total of 2 balloon per minute
    total_minutes = 30 # 30 minutes
    kris_total = kris_balloons_per_min * total_minutes

    # L2
    brother_speed_multiplier = 2 # her brother works twice as fast
    brother_balloons_per_min_first = kris_balloons_per_min * brother_speed_multiplier

    # L3
    first_half_minutes = 15 # After 15 minutes
    brother_balloons_first_half = brother_balloons_per_min_first * first_half_minutes

    # L4
    brother_speed_multiplier_second = 2 # brother doubles his speed
    brother_balloons_per_min_second = brother_balloons_per_min_first * brother_speed_multiplier_second

    # L5
    brother_balloons_second_half = brother_balloons_per_min_second * first_half_minutes

    # L6
    brother_total = brother_balloons_first_half + brother_balloons_second_half

    # L7
    total_balloons = kris_total + brother_total

    # FA
    answer = total_balloons
    return answer