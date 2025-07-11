def solve():
    """Index: 986.
    Returns: the difference in weekly swimming times between Susannah and Camden.
    """
    # L1
    camden_total_swims = 16 # Camden went swimming 16 times in March
    number_of_weeks = 4 # divided equally among 4 weeks
    camden_swims_per_week = camden_total_swims / number_of_weeks

    # L2
    susannah_total_swims = 24 # Susannah went 24 times
    susannah_swims_per_week = susannah_total_swims / number_of_weeks

    # L3
    difference_in_swims = susannah_swims_per_week - camden_swims_per_week

    # FA
    answer = difference_in_swims
    return answer