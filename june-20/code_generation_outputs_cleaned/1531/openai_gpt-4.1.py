def solve(
    years_working_out: int = 2, # it takes him 2 years of working out
    climbing_training_multiplier: int = 2, # spends twice that long learning how to be a technically proficient mountain climber
    num_summits: int = 7, # climb the seven summits
    months_per_mountain: int = 5, # spends 5 months climbing each mountain
    diving_training_months: int = 13, # takes 13 months learning to dive
    cave_diving_years: int = 2 # dives through all the caves he wants in 2 years
):
    """Index: 1531.
    Returns: the total number of years it took to complete all the goals.
    """
    #: L1
    climbing_training_years = years_working_out * climbing_training_multiplier

    #: L2
    total_climbing_months = months_per_mountain * num_summits

    #: L3
    months_before_diving = total_climbing_months + diving_training_months

    #: L4
    years_before_diving = months_before_diving / 12

    #: L5
    total_years = years_working_out + climbing_training_years + years_before_diving + cave_diving_years

    answer = total_years # FINAL ANSWER
    return answer