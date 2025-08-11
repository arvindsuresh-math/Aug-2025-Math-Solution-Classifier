def solve():
    """Index: 3875.
    Returns: the time it took for the third snail to race all the way up the sidewalk.
    """
    # L1
    first_snail_time = 20 # took the first snail 20 minutes
    second_snail_speed_multiplier = 2 # twice the speed of the first snail
    second_snail_time = first_snail_time / second_snail_speed_multiplier

    # L2
    third_snail_speed_multiplier = 5 # five times the rate of speed as the second snail
    third_snail_time = second_snail_time / third_snail_speed_multiplier

    # FA
    answer = third_snail_time
    return answer