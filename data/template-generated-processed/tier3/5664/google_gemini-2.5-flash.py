def solve():
    """Index: 5664.
    Returns: the total number of flowers Miriam can take care of in 6 days.
    """
    # L1
    hours_per_day = 5 # works 5 hours a day
    work_days = 6 # in 6 days of work
    total_hours_worked = hours_per_day * work_days

    # L2
    flowers_per_day = 60 # can take care of 60 different flowers in one day
    flowers_per_hour = flowers_per_day / hours_per_day

    # L3
    total_flowers_cared_for = total_hours_worked * flowers_per_hour

    # FA
    answer = total_flowers_cared_for
    return answer