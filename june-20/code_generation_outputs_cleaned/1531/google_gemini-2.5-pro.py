def solve(
    num_summits: int = 7, # one of his goals was to climb the seven summits
    workout_years: int = 2, # it takes him 2 years of working out
    months_per_mountain: int = 5, # He spends 5 months climbing each mountain
    months_learning_to_dive: int = 13, # he takes 13 months learning to dive
    diving_years: int = 2 # dives through all the caves he wants in 2 years
):
    """Index: 1531.
    Returns: the total time in years to get through all these goals.
    """
    #: L1
    years_learning_to_climb = workout_years * 2

    #: L2
    total_climbing_months = months_per_mountain * num_summits

    #: L3
    months_climbing_and_diving_prep = total_climbing_months + months_learning_to_dive

    #: L4
    years_climbing_and_diving_prep = months_climbing_and_diving_prep / 12

    #: L5
    total_years = workout_years + years_learning_to_climb + years_climbing_and_diving_prep + diving_years

    answer = total_years # FINAL ANSWER
    return answer