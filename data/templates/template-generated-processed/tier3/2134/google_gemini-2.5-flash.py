def solve():
    """Index: 2134.
    Returns: the number of additional cans needed to reach the project goal.
    """
    # L1
    martha_cans = 90 # Martha collected 90 cans
    half_divisor = 2 # half the cans
    half_martha_cans = martha_cans / half_divisor

    # L2
    diego_additional_cans = 10 # 10 more than half the cans
    diego_cans = half_martha_cans + diego_additional_cans

    # L3
    total_collected_by_martha_diego = martha_cans + diego_cans

    # L4
    project_goal = 150 # collect a total of 150 cans
    cans_needed = project_goal - total_collected_by_martha_diego

    # FA
    answer = cans_needed
    return answer