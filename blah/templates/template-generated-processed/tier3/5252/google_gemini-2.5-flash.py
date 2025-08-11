def solve():
    """Index: 5252.
    Returns: the number of parents who rated Needs Improvement.
    """
    # L1
    excellent_percentage = 15 # Fifteen percent of the respondents rated Excellent
    very_satisfactory_percentage = 60 # 60% rated Very Satisfactory
    total_excellent_very_satisfactory_percentage = excellent_percentage + very_satisfactory_percentage

    # L2
    total_parents = 120 # 120 parents answered the survey
    percentage_denominator = 100 # WK
    num_excellent_very_satisfactory = total_parents * total_excellent_very_satisfactory_percentage / percentage_denominator

    # L3
    remaining_parents = total_parents - num_excellent_very_satisfactory

    # L4
    satisfactory_percentage = 80 # 80% of the remaining respondents rated Satisfactory
    num_satisfactory = remaining_parents * satisfactory_percentage / percentage_denominator

    # L5
    num_needs_improvement = remaining_parents - num_satisfactory

    # FA
    answer = num_needs_improvement
    return answer