def solve():
    """Index: 4033.
    Returns: the total number of roses sent.
    """
    # L1
    num_dozen_per_day = 2 # 2 dozen roses every day
    dozen = 12 # WK
    roses_per_day = num_dozen_per_day * dozen

    # L2
    days_in_week = 7 # WK
    total_roses = roses_per_day * days_in_week

    # FA
    answer = total_roses
    return answer