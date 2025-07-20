def solve():
    """Index: 5655.
    Returns: the total number of boxes of milk Lolita drinks per week.
    """
    # L1
    milk_per_weekday = 3 # 3 boxes of milk during weekdays
    weekdays_in_week = 5 # WK
    total_milk_weekdays = milk_per_weekday * weekdays_in_week

    # L2
    saturday_multiplier = 2 # twice the number of boxes of milk
    total_milk_saturday = milk_per_weekday * saturday_multiplier

    # L3
    sunday_multiplier = 3 # thrice the number of boxes of milk
    total_milk_sunday = milk_per_weekday * sunday_multiplier

    # L4
    total_milk_per_week = total_milk_weekdays + total_milk_saturday + total_milk_sunday

    # FA
    answer = total_milk_per_week
    return answer