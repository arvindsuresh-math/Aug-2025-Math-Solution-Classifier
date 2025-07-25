def solve():
    """Index: 3879.
    Returns: the total number of pizza doughs Bruce can make in a week.
    """
    # L1
    batches_per_sack = 15 # 15 batches of pizza dough
    sacks_per_day = 5 # 5 sacks of flour per day
    batches_per_day = batches_per_sack * sacks_per_day

    # L2
    days_in_week = 7 # WK
    total_batches_per_week = batches_per_day * days_in_week

    # FA
    answer = total_batches_per_week
    return answer