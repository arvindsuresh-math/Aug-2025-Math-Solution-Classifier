def solve():
    """Index: 5609.
    Returns: the number of days until John finishes the game.
    """
    # L1
    days_per_week = 7 # WK
    num_weeks = 2 # 2 weeks
    total_days_played = days_per_week * num_weeks

    # L2
    hours_per_day_initial = 4 # 4 hours a day
    total_hours_played_initial = total_days_played * hours_per_day_initial

    # L3
    percent_done = 0.4 # 40% done
    total_game_length = total_hours_played_initial / percent_done

    # L4
    remaining_hours = total_game_length - total_hours_played_initial

    # L5
    hours_per_day_increased = 7 # 7 hours a day
    days_to_finish = remaining_hours / hours_per_day_increased

    # FA
    answer = days_to_finish
    return answer