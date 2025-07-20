def solve():
    """Index: 6157.
    Returns: the total number of people who have reappeared.
    """
    # L1
    total_performances = 100 # 100 performances of the act this year
    no_reappear_divisor = 10 # one-tenth of the time
    times_no_reappear = total_performances / no_reappear_divisor

    # L2
    two_people_reappear_divisor = 5 # one-fifth of the time
    times_two_reappear = total_performances / two_people_reappear_divisor

    # L3
    people_per_two_reappear_event = 2 # two people reappear
    people_from_two_reappear_events = people_per_two_reappear_event * times_two_reappear

    # L4
    times_one_reappear = total_performances - times_no_reappear - times_two_reappear

    # L5
    total_people_reappeared = times_one_reappear + people_from_two_reappear_events

    # FA
    answer = total_people_reappeared
    return answer