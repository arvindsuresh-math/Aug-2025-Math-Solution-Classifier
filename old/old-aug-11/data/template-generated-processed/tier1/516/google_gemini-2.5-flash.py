def solve():
    """Index: 516.
    Returns: the total time Max spent on doing his homework.
    """
    # L1
    biology_time = 20 # 20 minutes to finish tasks from biology
    history_multiplier = 2 # two times more time to finish history
    history_time = biology_time * history_multiplier

    # L2
    geography_multiplier = 3 # three times more than history
    geography_time = history_time * geography_multiplier

    # L3
    total_time = biology_time + history_time + geography_time

    # FA
    answer = total_time
    return answer