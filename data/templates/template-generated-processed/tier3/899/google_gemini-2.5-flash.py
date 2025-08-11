def solve():
    """Index: 899.
    Returns: the total number of chairs Ben can build.
    """
    # L1
    hours_per_day = 8 # 8-hour shifts
    number_of_days = 10 # in 10 days
    total_hours_worked = hours_per_day * number_of_days

    # L2
    hours_per_chair = 5 # 5 hours to build 1 rocking chair
    total_chairs_built = total_hours_worked / hours_per_chair

    # FA
    answer = total_chairs_built
    return answer