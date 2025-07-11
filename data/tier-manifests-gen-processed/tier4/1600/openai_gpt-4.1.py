def solve():
    """Index: 1600.
    Returns: the number of minnows with white bellies.
    """
    # L1
    red_minnows = 20 # 20 minnows have red bellies
    red_percent_num = 40 # 40% of the minnows have red bellies
    percent_factor = 0.01 # WK
    total_minnows = red_minnows / (red_percent_num * percent_factor)

    # L2
    green_percent_num = 30 # 30% have green bellies
    total_percent = 100 # WK
    white_percent_num = total_percent - red_percent_num - green_percent_num

    # L3
    white_minnows = white_percent_num * percent_factor * total_minnows

    # FA
    answer = white_minnows
    return answer