def solve():
    """Index: 4202.
    Returns: the time it takes to make the dough and cool the cookies.
    """
    # L1
    bake_time = 15 # bake the cookies for 15 minutes
    white_icing_harden_time = 30 # allow the icing to harden for 30 minutes
    chocolate_icing_harden_time = 30 # allowed to harden for an additional 30 minutes
    total_fixed_time = bake_time + white_icing_harden_time + chocolate_icing_harden_time

    # L2
    minutes_per_hour = 60 # WK
    total_hours = 2 # 2 hours to make the cookies from start to finish
    total_time_in_minutes = minutes_per_hour * total_hours

    # L3
    dough_and_cool_time = total_time_in_minutes - total_fixed_time

    # FA
    answer = dough_and_cool_time
    return answer