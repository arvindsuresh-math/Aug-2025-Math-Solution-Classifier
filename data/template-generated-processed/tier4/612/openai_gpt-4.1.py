def solve():
    """Index: 612.
    Returns: the percentage of bottle caps that are green.
    """
    # L1
    total_caps = 125 # Ali has 125 bottle caps
    red_caps = 50 # he has 50 red caps
    green_caps = total_caps - red_caps

    # L2
    green_proportion = green_caps / total_caps

    # L3
    percent_multiplier = 100 # WK
    green_percent = green_proportion * percent_multiplier

    # FA
    answer = green_percent
    return answer