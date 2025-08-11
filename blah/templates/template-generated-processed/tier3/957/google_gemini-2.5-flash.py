def solve():
    """Index: 957.
    Returns: the total time the grill ran in minutes.
    """
    # L1
    num_bags = 3 # three bags of coals
    coals_per_bag = 60 # Each bag of coal contains 60 coals
    total_coals_burned = num_bags * coals_per_bag

    # L2
    coals_burned_per_interval = 15 # burns fifteen coals
    minutes_per_interval = 20 # every twenty minutes
    total_minutes_ran = total_coals_burned / coals_burned_per_interval * minutes_per_interval

    # FA
    answer = total_minutes_ran
    return answer