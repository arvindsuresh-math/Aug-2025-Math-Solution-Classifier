def solve():
    """Index: 348.
    Returns: the final time Brian can hold his breath after three weeks of practice.
    """
    # L1
    initial_time = 10 # can only hold his breath underwater for 10 seconds
    double_factor = 2 # doubled
    first_week_time = initial_time * double_factor

    # L2
    second_week_time = first_week_time * double_factor

    # L3
    percent_increase = 0.5 # increased it by 50%
    third_week_increase = second_week_time * percent_increase

    # L4
    final_time = second_week_time + third_week_increase

    # FA
    answer = final_time
    return answer