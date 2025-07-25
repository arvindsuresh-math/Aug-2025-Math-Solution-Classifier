def solve():
    """Index: 1531.
    Returns: the total time taken to get through all the goals in years.
    """
    # L1
    workout_years = 2 # 2 years of working out
    climbing_multiplier = 2 # twice that long
    learning_to_climb_years = workout_years * climbing_multiplier

    # L2
    months_per_mountain = 5 # 5 months climbing each mountain
    num_mountains = 7 # climb the seven summits
    total_climbing_months = months_per_mountain * num_mountains

    # L3
    diving_learning_months = 13 # 13 months learning to dive
    total_months_before_diving_completion = total_climbing_months + diving_learning_months

    # L4
    months_per_year = 12 # WK
    total_years_from_climbing_and_diving_learning = total_months_before_diving_completion / months_per_year

    # L5
    diving_completion_years = 2 # dives through all the caves he wants in 2 years
    total_time_taken = workout_years + learning_to_climb_years + total_years_from_climbing_and_diving_learning + diving_completion_years

    # FA
    answer = total_time_taken
    return answer