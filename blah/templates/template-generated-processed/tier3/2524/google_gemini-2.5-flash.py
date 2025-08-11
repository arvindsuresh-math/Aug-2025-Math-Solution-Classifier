def solve():
    """Index: 2524.
    Returns: the difference between balloons touching the ceiling and not.
    """
    # L1
    helium_per_balloon = 50 # One balloon needs 50cm³ to float
    total_helium_volume = 1800 # 1800cm³ of helium
    balloons_touching_ceiling = total_helium_volume / helium_per_balloon

    # L2
    total_balloons = 50 # bought 50 balloons
    balloons_not_floating = total_balloons - balloons_touching_ceiling

    # L3
    difference_floating_not_floating = balloons_touching_ceiling - balloons_not_floating

    # FA
    answer = difference_floating_not_floating
    return answer