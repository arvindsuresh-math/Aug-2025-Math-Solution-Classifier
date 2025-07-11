def solve():
    """Index: 598.
    Returns: the cups of vegetables Sarah needs to eat per day to meet her weekly minimum requirement.
    """
    # L1
    days_in_week = 7 # WK
    recommended_cups_per_day = 2 # Federal guidelines recommend eating at least 2 cups of vegetables per day
    total_recommended_cups_week = days_in_week * recommended_cups_per_day

    # L2
    cups_eaten_so_far = 8 # Sarah has eaten 8 cups
    cups_left_to_eat = total_recommended_cups_week - cups_eaten_so_far

    # L3
    days_passed = 5 # From breakfast on Sunday to the end of the day on Thursday
    days_left_in_week = days_in_week - days_passed

    # L4
    cups_per_day_needed = cups_left_to_eat / days_left_in_week

    # FA
    answer = cups_per_day_needed
    return answer