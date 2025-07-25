def solve():
    """Index: 5924.
    Returns: the total number of apples Sam eats in one week.
    """
    # L1
    days_in_week = 7 # WK
    sandwiches_per_day = 10 # 10 sandwiches every day
    total_sandwiches = days_in_week * sandwiches_per_day

    # L2
    apples_per_sandwich = 4 # four apples
    total_apples = total_sandwiches * apples_per_sandwich

    # FA
    answer = total_apples
    return answer