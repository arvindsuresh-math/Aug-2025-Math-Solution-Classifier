def solve(
    workout_years: int = 2,  # "2 years of working out to get healthy enough to take up mountain climbing."
    learning_multiplier: int = 2,  # "twice that long learning how to be a technically proficient mountain climber."
    num_mountains: int = 7,  # "climb the seven summits."
    climb_months_per_mountain: int = 5,  # "spends 5 months climbing each mountain."
    learning_diving_months: int = 13,  # "takes 13 months learning to dive."
    diving_years: int = 2  # "dives through all the caves he wants in 2 years."
):
    """Index: 1531.
    Returns: the total time in years to complete all goals.
    """
    #: L1
    training_years = workout_years * learning_multiplier  # 2*2 = 4 years
    
    #: L2
    climb_months = num_mountains * climb_months_per_mountain  # 7*5 = 35 months
    
    #: L3
    combined_climb_diving_months = climb_months + learning_diving_months  # 35+13 = 48 months
    
    #: L4
    combined_climb_diving_years = combined_climb_diving_months / 12  # 48/12 = 4 years
    
    #: L5
    total_years = workout_years + training_years + combined_climb_diving_years + diving_years  # 2+4+4+2 = 12 years
    
    answer = total_years  # FINAL ANSWER
    return answer