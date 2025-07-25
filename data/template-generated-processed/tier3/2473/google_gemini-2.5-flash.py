def solve():
    """Index: 2473.
    Returns: the time it will take Rachel to paint the house.
    """
    # L1
    matt_hours = 12 # Matt can paint a house in 12 hours
    patty_time_divisor = 3 # Patty can paint the same house in one third the time
    patty_hours = matt_hours / patty_time_divisor

    # L2
    rachel_extra_hours = 5 # 5 more
    rachel_multiplier = 2 # double the amount of hours as Patty
    rachel_hours = rachel_extra_hours + rachel_multiplier * patty_hours

    # FA
    answer = rachel_hours
    return answer