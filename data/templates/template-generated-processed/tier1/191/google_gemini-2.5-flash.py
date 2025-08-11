def solve():
    """Index: 191.
    Returns: the total number of weasels and rabbits left after 3 weeks.
    """
    # L1
    num_foxes = 3 # Three foxes
    weasels_per_fox_per_week = 4 # 4 weasels
    total_weasels_caught_per_week = num_foxes * weasels_per_fox_per_week

    # L2
    num_weeks = 3 # 3 weeks
    total_weasels_caught_overall = total_weasels_caught_per_week * num_weeks

    # L3
    rabbits_per_fox_per_week = 2 # 2 rabbits
    total_rabbits_caught_per_week = num_foxes * rabbits_per_fox_per_week

    # L4
    total_rabbits_caught_overall = total_rabbits_caught_per_week * num_weeks

    # L5
    initial_weasels = 100 # 100 weasels
    weasels_left = initial_weasels - total_weasels_caught_overall

    # L6
    initial_rabbits = 50 # 50 rabbits
    rabbits_left = initial_rabbits - total_rabbits_caught_overall

    # L7
    total_animals_left = weasels_left + rabbits_left

    # FA
    answer = total_animals_left
    return answer