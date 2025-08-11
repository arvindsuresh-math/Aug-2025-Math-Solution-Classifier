def solve():
    """Index: 191.
    Returns: the total number of rabbits and weasels left after 3 weeks.
    """
    # L1
    num_foxes = 3 # Three foxes invade this region
    weasels_per_fox_per_week = 4 # Each fox catches an average of 4 weasels
    weasels_caught_per_week = num_foxes * weasels_per_fox_per_week

    # L2
    num_weeks = 3 # after 3 weeks
    total_weasels_caught = weasels_caught_per_week * num_weeks

    # L3
    rabbits_per_fox_per_week = 2 # Each fox catches an average of 2 rabbits
    rabbits_caught_per_week = num_foxes * rabbits_per_fox_per_week

    # L4
    total_rabbits_caught = rabbits_caught_per_week * num_weeks

    # L5
    initial_weasels = 100 # there are 100 weasels
    weasels_left = initial_weasels - total_weasels_caught

    # L6
    initial_rabbits = 50 # there are 50 rabbits
    rabbits_left = initial_rabbits - total_rabbits_caught

    # L7
    total_left = weasels_left + rabbits_left

    # FA
    answer = total_left
    return answer