def solve():
    """Index: 5674.
    Returns: the maximum number of alligators the snake can eat.
    """
    # L1
    total_days = 616 # 616 days
    days_per_week = 7 # one week is 7 days
    total_weeks = total_days / days_per_week

    # L2
    alligators_per_week = 1 # eats 1 alligator per week
    max_alligators = total_weeks / alligators_per_week

    # FA
    answer = max_alligators
    return answer