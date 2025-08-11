def solve():
    """Index: 2463.
    Returns: the difference in the total number of athletes in the camp over the two nights.
    """
    # L1
    hours_left = 4 # for 4 hours straight, they left
    rate_left = 28 # at a rate of 28 athletes per hour
    num_left = hours_left * rate_left

    # L2
    initial_athletes = 300 # A group of 300 athletes spent Saturday night
    remaining_after_left = initial_athletes - num_left

    # L3
    hours_in = 7 # over the next 7 hours
    rate_in = 15 # at a rate of 15 athletes per hour
    num_in = hours_in * rate_in

    # L4
    sunday_night_athletes = remaining_after_left + num_in

    # L5
    difference = initial_athletes - sunday_night_athletes

    # FA
    answer = difference
    return answer