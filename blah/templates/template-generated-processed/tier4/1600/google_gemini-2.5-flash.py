def solve():
    """Index: 1600.
    Returns: the number of minnows with white bellies.
    """
    # L1
    red_minnows_count = 20 # 20 minnows have red bellies
    red_belly_percentage_value = 40 # 40% of the minnows have red bellies
    percent_divisor = 100 # WK
    total_minnows = red_minnows_count / (red_belly_percentage_value / percent_divisor)

    # L2
    total_percentage = 100 # WK
    green_belly_percentage_value = 30 # 30% have green bellies
    white_belly_percentage_value = total_percentage - red_belly_percentage_value - green_belly_percentage_value

    # L3
    percent_factor = 0.01 # WK
    white_belly_minnows_count = white_belly_percentage_value * percent_factor * total_minnows

    # FA
    answer = white_belly_minnows_count
    return answer