def solve():
    """Index: 5985.
    Returns: the total hours Billy slept in the four day period.
    """
    # L1
    first_night_sleep = 6 # 6 hours one night
    additional_hours_second_night = 2 # 2 more hours than that
    second_night_sleep = first_night_sleep + additional_hours_second_night

    # L2
    half_divisor = 2 # half the previous amount
    third_night_sleep = second_night_sleep / half_divisor

    # L3
    triple_multiplier = 3 # triple the previous amount
    fourth_night_sleep = third_night_sleep * triple_multiplier

    # L4
    total_sleep = first_night_sleep + second_night_sleep + third_night_sleep + fourth_night_sleep

    # FA
    answer = total_sleep
    return answer