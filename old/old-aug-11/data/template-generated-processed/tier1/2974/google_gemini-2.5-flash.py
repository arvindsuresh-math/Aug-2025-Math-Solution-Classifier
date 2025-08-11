def solve():
    """Index: 2974.
    Returns: the total time James spent to become a master.
    """
    # L1
    time_to_learn_rules = 2 # 2 hours to learn the rules
    proficiency_multiplier = 49 # 49 times that long
    time_to_proficiency = time_to_learn_rules * proficiency_multiplier

    # L2
    combined_time_to_proficient = time_to_proficiency + time_to_learn_rules

    # L3
    master_multiplier = 100 # 100 times as much as the combined time
    time_to_master = master_multiplier * combined_time_to_proficient

    # L4
    total_time = combined_time_to_proficient + time_to_master

    # FA
    answer = total_time
    return answer