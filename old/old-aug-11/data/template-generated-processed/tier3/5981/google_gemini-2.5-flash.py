def solve():
    """Index: 5981.
    Returns: the total hours it will take to download all files.
    """
    # L1
    file_size_1 = 80 # size of 80 megabits
    internet_speed = 2 # 2 megabits per minute
    time_file_1 = file_size_1 / internet_speed

    # L2
    file_size_2 = 90 # 90 megabits
    time_file_2 = file_size_2 / internet_speed

    # L3
    file_size_3 = 70 # and 70 megabits
    time_file_3 = file_size_3 / internet_speed

    # L4
    total_minutes = time_file_1 + time_file_2 + time_file_3

    # L5
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer