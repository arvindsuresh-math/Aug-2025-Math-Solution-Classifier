def solve():
    """Index: 6677.
    Returns: the number of additional minutes Justin needs to look for flowers.
    """
    # L1
    hours_gathering = 2 # 2 hours
    minutes_per_hour = 60 # WK
    minutes_gathering = hours_gathering * minutes_per_hour

    # L2
    minutes_per_flower = 10 # 10 minutes to find a flower
    flowers_gathered_initial = minutes_gathering / minutes_per_flower

    # L3
    flowers_lost = 3 # lost 3 of the flowers
    flowers_kept = flowers_gathered_initial - flowers_lost

    # L4
    total_classmates = 30 # 30 classmates
    flowers_needed_additional = total_classmates - flowers_kept

    # L5
    minutes_needed_additional = minutes_per_flower * flowers_needed_additional

    # FA
    answer = minutes_needed_additional
    return answer