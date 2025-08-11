def solve():
    """Index: 4178.
    Returns: the total time taken for everything.
    """
    # L1
    years_learning_basics = 2 # 2 years learning the basics of his field
    research_extra_percent = 0.75 # 75% more time on research
    extra_research_time = years_learning_basics * research_extra_percent

    # L2
    total_research_time = years_learning_basics + extra_research_time

    # L3
    acclimation_period = 1 # 1 year of courses to get acclimated
    half_divisor = 2 # half as long on writing his dissertation
    dissertation_time = acclimation_period / half_divisor

    # L4
    total_time = acclimation_period + years_learning_basics + total_research_time + dissertation_time

    # FA
    answer = total_time
    return answer