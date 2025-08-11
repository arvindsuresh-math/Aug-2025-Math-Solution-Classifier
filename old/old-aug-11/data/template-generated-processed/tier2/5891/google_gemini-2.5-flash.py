def solve():
    """Index: 5891.
    Returns: the total amount of goals both teams scored.
    """
    # L1
    kickers_first_period_goals = 2 # scored 2 goals in the first period
    twice_factor = 2 # twice that amount
    kickers_second_period_goals = twice_factor * kickers_first_period_goals

    # L2
    half_factor = 0.5 # half the amount
    spiders_first_period_goals = half_factor * kickers_first_period_goals

    # L3
    spiders_second_period_goals = twice_factor * kickers_second_period_goals

    # L4
    total_goals = kickers_first_period_goals + kickers_second_period_goals + spiders_first_period_goals + spiders_second_period_goals

    # FA
    answer = total_goals
    return answer