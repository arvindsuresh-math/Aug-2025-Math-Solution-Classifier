def solve():
    """Index: 348.
    Returns: how long Brian can hold his breath for now.
    """
    # L1
    initial_breath_hold_time = 10 # 10 seconds
    doubling_factor = 2 # doubled the amount of time
    first_week_time = initial_breath_hold_time * doubling_factor

    # L2
    second_week_time = first_week_time * doubling_factor

    # L3
    increase_percent_decimal = 0.5 # increased it by 50%
    third_week_increase = second_week_time * increase_percent_decimal

    # L4
    final_breath_hold_time = second_week_time + third_week_increase

    # FA
    answer = final_breath_hold_time
    return answer