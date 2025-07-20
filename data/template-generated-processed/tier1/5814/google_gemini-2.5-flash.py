def solve():
    """Index: 5814.
    Returns: the number of minutes Hillary has to read on Sunday.
    """
    # L1
    assignment_hours = 1 # 1 hour of reading
    minutes_per_hour = 60 # WK
    total_assignment_minutes = assignment_hours * minutes_per_hour

    # L2
    read_friday = 16 # read for 16 minutes
    read_saturday = 28 # read for 28 minutes
    read_so_far = read_friday + read_saturday

    # L3
    remaining_minutes_sunday = total_assignment_minutes - read_so_far

    # FA
    answer = remaining_minutes_sunday
    return answer