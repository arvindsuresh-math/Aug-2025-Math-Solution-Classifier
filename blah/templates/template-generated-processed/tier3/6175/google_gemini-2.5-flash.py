def solve():
    """Index: 6175.
    Returns: the average number of goals scored by Layla and Kristin.
    """
    # L1
    layla_goals = 104 # Layla scored 104 goals
    kristin_fewer_goals = 24 # Kristin scored 24 fewer goals
    kristin_goals = layla_goals - kristin_fewer_goals

    # L2
    combined_goals = kristin_goals + layla_goals

    # L3
    number_of_players = 2 # the two scored
    average_goals = combined_goals / number_of_players

    # FA
    answer = average_goals
    return answer