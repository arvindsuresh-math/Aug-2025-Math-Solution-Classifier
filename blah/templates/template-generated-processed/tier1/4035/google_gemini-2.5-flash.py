def solve():
    """Index: 4035.
    Returns: the total pounds of pig feed Randy's pigs will be fed per week.
    """
    # L1
    num_pigs = 2 # If Randy has 2 pigs
    days_per_week = 7 # WK
    total_feedings = days_per_week * num_pigs

    # L2
    pounds_per_feeding = 10 # 10 pounds of feed per pig per day
    total_feed_per_week = pounds_per_feeding * total_feedings

    # FA
    answer = total_feed_per_week
    return answer