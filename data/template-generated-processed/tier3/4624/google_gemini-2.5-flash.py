def solve():
    """Index: 4624.
    Returns: the acres of cotton each tractor needs to plant per day.
    """
    # L1
    num_tractors_crew1 = 2 # a crew of 2 tractors
    days_crew1 = 2 # working for 2 days
    tractor_days_crew1 = num_tractors_crew1 * days_crew1

    # L2
    num_tractors_crew2 = 7 # a crew of 7 tractors
    days_crew2 = 3 # working for another 3 days
    tractor_days_crew2 = num_tractors_crew2 * days_crew2

    # L3
    total_tractor_days = tractor_days_crew1 + tractor_days_crew2

    # L4
    total_acres = 1700 # 1700 acres of cotton
    acres_per_tractor_day = total_acres / total_tractor_days

    # FA
    answer = acres_per_tractor_day
    return answer