def solve():
    """Index: 5714.
    Returns: the total number of jalapeno peppers required.
    """
    # L1
    strips_per_sandwich = 4 # four strips of jalapeno pepper
    slices_per_pepper = 8 # a single jalapeno pepper makes 8 slices
    pepper_per_sandwich = strips_per_sandwich / slices_per_pepper

    # L2
    minutes_per_sandwich = 5 # serves a sandwich every 5 minutes
    minutes_per_hour = 60 # WK
    sandwiches_per_hour = minutes_per_hour / minutes_per_sandwich

    # L3
    peppers_per_hour = sandwiches_per_hour * pepper_per_sandwich

    # L4
    hours_in_day = 8 # an 8-hour day
    total_peppers_required = hours_in_day * peppers_per_hour

    # FA
    answer = total_peppers_required
    return answer