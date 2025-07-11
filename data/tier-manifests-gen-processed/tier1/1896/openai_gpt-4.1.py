def solve():
    """Index: 1896.
    Returns: the total number of goals Bruce and Michael both scored.
    """
    # L1
    bruce_goals = 4 # Bruce scored 4 goals

    # L2
    michael_multiplier = 3 # Michael scored 3 times more than Bruce
    michael_goals = bruce_goals * michael_multiplier

    # L3
    total_goals = michael_goals + bruce_goals

    # FA
    answer = total_goals
    return answer