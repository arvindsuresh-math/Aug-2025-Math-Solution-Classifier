def solve():
    """Index: 3903.
    Returns: the total number of face-masks Manolo makes.
    """
    # L1
    minutes_per_hour = 60 # WK
    first_hour_rate_minutes = 4 # one every four minutes
    masks_first_hour = minutes_per_hour / first_hour_rate_minutes

    # L2
    subsequent_hour_rate_minutes = 6 # one every six minutes
    masks_subsequent_hour = minutes_per_hour / subsequent_hour_rate_minutes

    # L3
    total_shift_hours = 4 # four-hour shift
    first_hour_duration = 1 # first hour of work
    remaining_hours = total_shift_hours - first_hour_duration

    # L4
    total_masks = masks_first_hour + masks_subsequent_hour * remaining_hours

    # FA
    answer = total_masks
    return answer