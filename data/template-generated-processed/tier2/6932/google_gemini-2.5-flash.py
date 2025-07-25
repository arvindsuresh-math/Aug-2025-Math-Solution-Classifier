def solve():
    """Index: 6932.
    Returns: the number of additional minutes of video game time Diana will get as a result of her raise.
    """
    # L1
    initial_reward_per_hour = 30 # 30 minutes of video game time
    raise_percent_text = 20 # raise her reward by 20%
    raise_percent_decimal = 0.20 # from solution text: 0.20 x 30
    percent_factor = 0.01 # WK
    raise_amount_per_hour = raise_percent_text * percent_factor * initial_reward_per_hour

    # L2
    new_reward_per_hour = initial_reward_per_hour + raise_amount_per_hour

    # L3
    hours_read = 12 # read for 12 hours
    total_new_reward = hours_read * new_reward_per_hour

    # L4
    total_old_reward = hours_read * initial_reward_per_hour

    # L5
    additional_minutes = total_new_reward - total_old_reward

    # FA
    answer = additional_minutes
    return answer