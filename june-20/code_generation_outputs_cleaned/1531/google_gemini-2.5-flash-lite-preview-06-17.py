def solve(
    initial_workout_years: int = 2, # it takes him 2 years of working out
    months_climbing_each_mountain: int = 5, # He spends 5 months climbing each mountain
    num_summits: int = 7, # climb the seven summits
    months_learning_to_dive: int = 13, # takes 13 months learning to dive
    years_diving: int = 2 # dives through all the caves he wants in 2 years
):
    """Index: 1531.
    Returns: the total time in years it took to complete all the goals.
    """
    #: L1
    years_learning_to_climb = initial_workout_years * 2

    #: L2
    months_climbing_all_mountains = months_climbing_each_mountain * num_summits

    #: L3
    total_months_before_diving = months_climbing_all_mountains + months_learning_to_dive

    #: L4
    years_before_diving = total_months_before_diving / 12

    #: L5
    total_years = initial_workout_years + years_learning_to_climb + years_before_diving + years_diving

    answer = total_years # FINAL ANSWER
    return answer