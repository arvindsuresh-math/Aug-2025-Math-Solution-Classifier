def solve():
    """Index: 2463.
    Returns: the difference in the total number of athletes in the camp over the two nights.
    """
    # L1
    hours_leaving = 4 # for 4 hours straight
    rate_leaving = 28 # at a rate of 28 athletes per hour
    athletes_left = hours_leaving * rate_leaving

    # L2
    initial_athletes = 300 # A group of 300 athletes
    athletes_remaining_after_leaving = initial_athletes - athletes_left

    # L3
    hours_trickling_in = 7 # Over the next 7 hours
    rate_trickling_in = 15 # at a rate of 15 athletes per hour
    new_athletes_arrived = hours_trickling_in * rate_trickling_in

    # L4
    athletes_sunday_night = athletes_remaining_after_leaving + new_athletes_arrived

    # L5
    difference_in_athletes = initial_athletes - athletes_sunday_night

    # FA
    answer = difference_in_athletes
    return answer