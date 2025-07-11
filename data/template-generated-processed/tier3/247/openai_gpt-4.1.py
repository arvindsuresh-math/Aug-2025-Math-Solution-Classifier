def solve():
    """Index: 247.
    Returns: the number of pills left in the bottle after Tony's usage.
    """
    # L1
    initial_pills = 50 # a bottle of 50 pills
    pills_per_dose = 2 # takes 2 pills each
    doses_per_day = 3 # three times a day
    pills_per_day_initial = pills_per_dose * doses_per_day

    # L2
    days_initial = 2 # for the first 2 days
    pills_first_period = days_initial * pills_per_day_initial

    # L3
    pills_per_day_reduced = pills_per_day_initial / 2

    # L4
    days_reduced = 3 # for the next 3 days
    pills_second_period = pills_per_day_reduced * days_reduced

    # L5
    final_day_pills = 2 # On the sixth day, he takes a final 2 pills
    total_pills_taken = pills_first_period + pills_second_period + final_day_pills

    # L6
    answer = initial_pills - total_pills_taken
    return answer