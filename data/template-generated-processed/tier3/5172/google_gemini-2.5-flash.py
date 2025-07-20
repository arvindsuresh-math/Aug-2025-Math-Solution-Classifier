def solve():
    """Index: 5172.
    Returns: the percentage of exercises that were pushups.
    """
    # L1
    jumping_jacks = 12 # 12 jumping jacks
    pushups = 8 # 8 pushups
    situps = 20 # 20 situps
    total_exercises = jumping_jacks + pushups + situps

    # L2
    percentage_multiplier = 100 # WK
    percentage_pushups = (pushups / total_exercises) * percentage_multiplier

    # FA
    answer = percentage_pushups
    return answer