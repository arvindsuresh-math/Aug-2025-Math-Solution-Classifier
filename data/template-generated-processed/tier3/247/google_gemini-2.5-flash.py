def solve():
    """Index: 247.
    Returns: the number of pills left in the bottle.
    """
    # L1
    initial_pills_in_bottle = 50 # bottle of 50 pills
    pills_per_dose = 2 # takes 2 pills each day
    doses_per_day = 3 # three times a day
    pills_per_day_initial_rate = pills_per_dose * doses_per_day

    # L2
    days_initial_rate = 2 # for the first 2 days
    total_pills_initial_period = days_initial_rate * pills_per_day_initial_rate

    # L3
    half_divisor = 2 # cutting this amount in half
    pills_per_day_reduced_rate = pills_per_day_initial_rate / half_divisor

    # L4
    days_reduced_rate = 3 # for the next 3 days
    total_pills_reduced_period = days_reduced_rate * pills_per_day_reduced_rate

    # L5
    final_day_pills = 2 # takes a final 2 pills
    total_pills_taken = total_pills_initial_period + total_pills_reduced_period + final_day_pills

    # L6
    pills_remaining = initial_pills_in_bottle - total_pills_taken

    # FA
    answer = pills_remaining
    return answer