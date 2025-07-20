def solve():
    """Index: 5418.
    Returns: the number of days ago there were less than 50 zombies.
    """
    # L1
    current_zombies = 480 # 480 zombies in the shopping mall
    doubling_factor = 2 # doubled every day
    zombies_one_day_ago = current_zombies / doubling_factor

    # L2
    zombies_two_days_ago = zombies_one_day_ago / doubling_factor

    # L3
    zombies_three_days_ago = zombies_two_days_ago / doubling_factor

    # L4
    threshold_zombies = 50 # less than 50 zombies
    days_count = 4 # 4 days ago
    zombies_four_days_ago = zombies_three_days_ago / doubling_factor

    # FA
    answer = days_count
    return answer