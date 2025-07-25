def solve():
    """Index: 3049.
    Returns: the number of minutes it took Andy to put away the laundry.
    """
    # L1
    dawn_minutes_dishes = 20 # 20 minutes to wash the dishes
    two_times_multiplier = 2 # two times the number of minutes
    dawn_minutes_doubled = dawn_minutes_dishes * two_times_multiplier

    # L2
    andy_additional_minutes = 6 # six minutes more
    andy_laundry_minutes = dawn_minutes_doubled + andy_additional_minutes

    # FA
    answer = andy_laundry_minutes
    return answer