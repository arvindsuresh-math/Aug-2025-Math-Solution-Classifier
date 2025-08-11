def solve():
    """Index: 2974.
    Returns: the total time James spent to become a chess grandmaster.
    """
    # L1
    hours_to_learn_rules = 2 # It takes 2 hours to learn the rules
    proficiency_multiplier = 49 # 49 times that long
    hours_to_proficient = hours_to_learn_rules * proficiency_multiplier

    # L2
    combined_hours = hours_to_proficient + hours_to_learn_rules

    # L3
    master_multiplier = 100 # 100 times as much as the combined time
    hours_to_master = combined_hours * master_multiplier

    # L4
    total_time = combined_hours + hours_to_master

    # FA
    answer = total_time
    return answer