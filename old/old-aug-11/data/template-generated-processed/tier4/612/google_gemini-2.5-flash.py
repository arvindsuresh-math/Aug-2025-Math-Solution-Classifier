def solve():
    """Index: 612.
    Returns: the percentage of caps that are green.
    """
    # L1
    total_caps = 125 # He has 125 bottle caps
    red_caps = 50 # He has 50 red caps
    green_caps = total_caps - red_caps

    # L2
    proportion_green = green_caps / total_caps

    # L3
    percent_multiplier = 100 # WK
    percentage_green = proportion_green * percent_multiplier

    # FA
    answer = percentage_green
    return answer