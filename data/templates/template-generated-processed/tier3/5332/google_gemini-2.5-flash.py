def solve():
    """Index: 5332.
    Returns: the average hours Max spent playing video games.
    """
    # L1
    wednesday_hours = 2 # 2 hours on Wednesday
    extra_friday_hours = 3 # three hours more
    friday_hours = wednesday_hours + extra_friday_hours

    # L2
    thursday_hours = 2 # the same time on Thursday
    total_hours = wednesday_hours + thursday_hours + friday_hours

    # L3
    number_of_days = 3 # during these three days
    average_hours = total_hours / number_of_days

    # FA
    answer = average_hours
    return answer