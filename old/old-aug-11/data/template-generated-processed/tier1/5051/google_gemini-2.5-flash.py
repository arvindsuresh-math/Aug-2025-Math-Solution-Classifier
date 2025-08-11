def solve():
    """Index: 5051.
    Returns: the total number of steps Eliana walked during these three days.
    """
    # L1
    initial_steps_morning = 200 # walked 200 steps for her morning exercise
    additional_steps_first_day = 300 # added some 300 more steps to her count for the first day
    steps_day1 = initial_steps_morning + additional_steps_first_day

    # L2
    multiplier_twice = 2 # walked twice the number of steps
    steps_day2 = multiplier_twice * steps_day1

    # L3
    total_steps_day1_day2 = steps_day2 + steps_day1

    # L4
    additional_steps_day3 = 100 # walked an additional 100 steps
    total_steps_three_days = total_steps_day1_day2 + additional_steps_day3

    # FA
    answer = total_steps_three_days
    return answer