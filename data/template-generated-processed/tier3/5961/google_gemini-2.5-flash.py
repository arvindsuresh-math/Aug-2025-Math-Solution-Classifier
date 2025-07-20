def solve():
    """Index: 5961.
    Returns: the total number of cars that passed the toll booth in each of the remaining days.
    """
    # L1
    cars_monday = 50 # Fifty vehicles went through the toll booth on Monday
    cars_tuesday = 50 # the same number of vehicles drove through the toll booth on Tuesday
    cars_mon_tue = cars_monday + cars_tuesday

    # L2
    multiplier_wednesday = 2 # twice the number of cars
    cars_wednesday = multiplier_wednesday * cars_monday

    # L3
    cars_wed_thu = cars_wednesday + cars_wednesday

    # L4
    cars_mon_to_thu = cars_wed_thu + cars_mon_tue

    # L5
    total_cars_week = 450 # 450 cars drove through a toll booth
    cars_remaining_days = total_cars_week - cars_mon_to_thu

    # L6
    remaining_days_count = 3 # remaining of the days of the week
    cars_per_remaining_day = cars_remaining_days / remaining_days_count

    # FA
    answer = cars_per_remaining_day
    return answer