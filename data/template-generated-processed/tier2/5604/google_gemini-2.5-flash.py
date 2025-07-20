def solve():
    """Index: 5604.
    Returns: the total number of goals scored by both teams during the whole match.
    """
    # L1
    team_a_first_half_score = 8 # Team A scored 8 points
    half_factor = 0.5 # half as many points
    team_b_first_half_score = team_a_first_half_score * half_factor

    # L2
    team_b_second_half_score = 8 # Team B was able to get as many points as Team A in the first half
    team_a_second_half_less_goals = 2 # 2 goals less
    team_a_second_half_score = team_b_second_half_score - team_a_second_half_less_goals

    # L3
    total_score = team_a_first_half_score + team_b_first_half_score + team_a_second_half_score + team_b_second_half_score

    # FA
    answer = total_score
    return answer