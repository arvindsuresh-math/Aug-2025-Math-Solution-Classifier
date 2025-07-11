def solve():
    """Index: 1308.
    Returns: the number of hours Jake watched on Friday.
    """
    # L1
    hours_per_day = 24 # WK
    monday_divisor = 2 # half the day on Monday
    monday_hours = hours_per_day / monday_divisor

    # L2
    wednesday_divisor = 4 # a quarter of the day on Wednesday
    wednesday_hours = hours_per_day / wednesday_divisor

    # L3
    tuesday_hours = 4 # 4 hours on Tuesday
    total_mon_wed_hours = monday_hours + tuesday_hours + wednesday_hours

    # L4
    thursday_divisor = 2 # half as much time watching the show on Thursday
    thursday_hours = total_mon_wed_hours / thursday_divisor

    # L5
    total_mon_thu_hours = total_mon_wed_hours + thursday_hours

    # L6
    total_show_length = 52 # entire show is 52 hours long
    friday_hours = total_show_length - total_mon_thu_hours

    # FA
    answer = friday_hours
    return answer