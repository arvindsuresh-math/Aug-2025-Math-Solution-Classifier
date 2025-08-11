def solve():
    """Index: 146.
    Returns: the total minutes all three spend cleaning their rooms each week.
    """
    # L1
    richard_time = 22 # Richard can clean his room in 22 minutes.
    cory_more_than_richard = 3 # 3 minutes more than Richard
    cory_time = richard_time + cory_more_than_richard

    # L2
    blake_quicker_than_cory = 4 # 4 minutes more quickly than Cory
    blake_time = cory_time - blake_quicker_than_cory

    # L3
    total_time_per_cleaning = richard_time + cory_time + blake_time

    # L4
    cleanings_per_week = 2 # twice a week
    total_weekly_cleaning_time = total_time_per_cleaning * cleanings_per_week

    # FA
    answer = total_weekly_cleaning_time
    return answer