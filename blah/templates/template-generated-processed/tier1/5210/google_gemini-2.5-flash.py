def solve():
    """Index: 5210.
    Returns: the milligrams of coffee Lisa drank over her goal.
    """
    # L1
    caffeine_per_cup = 80 # 80 mg of caffeine in a cup of coffee
    num_cups = 3 # three cups of coffee
    total_caffeine_drank = caffeine_per_cup * num_cups

    # L2
    caffeine_goal = 200 # not want to drink more than 200 mg of caffeine per day
    over_goal = total_caffeine_drank - caffeine_goal

    # FA
    answer = over_goal
    return answer