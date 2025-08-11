def solve():
    """Index: 7014.
    Returns: the number of balloons Claire has.
    """
    # L1
    given_one_balloon = 1 # 1 balloon to a little girl
    floated_away = 12 # 12 balloons floated away
    gave_away_more = 9 # gave 9 more away
    total_lost_balloons = given_one_balloon + floated_away + gave_away_more

    # L2
    started_balloons = 50 # started with 50 balloons
    remaining_after_loss = started_balloons - total_lost_balloons

    # L3
    coworker_balloons = 11 # last 11 from her coworker
    final_balloons = remaining_after_loss + coworker_balloons

    # FA
    answer = final_balloons
    return answer