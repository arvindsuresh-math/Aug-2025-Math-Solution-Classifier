def solve():
    """Index: 7045.
    Returns: the total spending money Jackson has earned.
    """
    # L1
    vacuuming_hours_per_session = 2 # spends 2 hours vacuuming
    vacuuming_sessions = 2 # do this twice
    total_vacuuming_hours = vacuuming_hours_per_session * vacuuming_sessions

    # L2
    money_per_hour = 5 # promises $5 per hour
    earnings_from_vacuuming = total_vacuuming_hours * money_per_hour

    # L3
    dish_washing_hours = 0.5 # spends 0.5 hours washing dishes
    earnings_from_dishes = dish_washing_hours * money_per_hour

    # L4
    bathroom_time_multiplier = 3 # three times as long
    bathroom_cleaning_hours = dish_washing_hours * bathroom_time_multiplier

    # L5
    earnings_from_bathroom = bathroom_cleaning_hours * money_per_hour

    # L6
    total_earnings = earnings_from_vacuuming + earnings_from_dishes + earnings_from_bathroom

    # FA
    answer = total_earnings
    return answer