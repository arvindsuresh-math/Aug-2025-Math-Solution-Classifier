def solve():
    """Index: 213.
    Returns: the total number of tomato seeds Mike and Ted planted altogether.
    """
    # L1
    mike_morning = 50 # Mike planted 50 tomato seeds
    ted_morning_multiplier = 2 # Ted planted twice as much as Mike
    ted_morning = ted_morning_multiplier * mike_morning

    # L2
    morning_total = mike_morning + ted_morning

    # L3
    mike_afternoon = 60 # Mike planted 60 tomato seeds
    ted_afternoon_fewer = 20 # Ted planted 20 fewer tomato seeds than Mike
    ted_afternoon = mike_afternoon - ted_afternoon_fewer

    # L4
    afternoon_total = mike_afternoon + ted_afternoon

    # L5
    total_seeds = morning_total + afternoon_total

    # FA
    answer = total_seeds
    return answer