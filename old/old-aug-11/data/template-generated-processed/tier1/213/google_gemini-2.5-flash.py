def solve():
    """Index: 213.
    Returns: the total number of tomato seeds planted by Mike and Ted.
    """
    # L1
    ted_multiplier = 2 # twice as much as Mike
    mike_morning_seeds = 50 # Mike planted 50 tomato seeds
    ted_morning_seeds = ted_multiplier * mike_morning_seeds

    # L2
    total_morning_seeds = mike_morning_seeds + ted_morning_seeds

    # L3
    mike_afternoon_seeds = 60 # Mike planted 60 tomato seeds
    ted_fewer_afternoon = 20 # 20 fewer tomato seeds than Mike
    ted_afternoon_seeds = mike_afternoon_seeds - ted_fewer_afternoon

    # L4
    total_afternoon_seeds = mike_afternoon_seeds + ted_afternoon_seeds

    # L5
    total_seeds_altogether = total_morning_seeds + total_afternoon_seeds

    # FA
    answer = total_seeds_altogether
    return answer