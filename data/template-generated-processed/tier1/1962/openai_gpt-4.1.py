def solve():
    """Index: 1962.
    Returns: the total number of paintings Philip will have after 30 days.
    """
    # L1
    paintings_per_day = 2 # makes 2 paintings per day
    num_days = 30 # after 30 days
    paintings_made = paintings_per_day * num_days

    # L2
    initial_paintings = 20 # already has 20 paintings
    total_paintings = paintings_made + initial_paintings

    # FA
    answer = total_paintings
    return answer