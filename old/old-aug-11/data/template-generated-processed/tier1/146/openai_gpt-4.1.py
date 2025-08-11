def solve():
    """Index: 146.
    Returns: the total minutes all three spend cleaning their rooms each week.
    """
    # L1
    richard_time = 22 # Richard can clean his room in 22 minutes
    cory_more_than_richard = 3 # Cory takes 3 minutes more than Richard
    cory_time = richard_time + cory_more_than_richard

    # L2
    blake_faster_than_cory = 4 # Blake can clean his room 4 minutes more quickly than Cory
    blake_time = cory_time - blake_faster_than_cory

    # L3
    total_one_clean = richard_time + cory_time + blake_time

    # L4
    times_per_week = 2 # clean their rooms twice a week
    total_weekly = total_one_clean * times_per_week

    # FA
    answer = total_weekly
    return answer