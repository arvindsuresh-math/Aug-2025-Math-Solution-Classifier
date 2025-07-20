def solve():
    """Index: 5583.
    Returns: the average number of points for the playoff teams.
    """
    # L1
    first_place_wins = 12 # 12 wins
    second_place_wins = 13 # 13 wins
    elsas_team_wins = 8 # 8 wins
    total_wins = first_place_wins + second_place_wins + elsas_team_wins

    # L2
    points_per_win = 2 # 2 points for a win
    points_from_wins = total_wins * points_per_win

    # L3
    first_place_ties = 4 # 4 ties
    second_place_ties = 1 # 1 tie
    elsas_team_ties = 10 # 10 ties
    total_ties = first_place_ties + second_place_ties + elsas_team_ties

    # L4
    points_per_tie = 1 # 1 point for a tie
    points_from_ties = total_ties * points_per_tie

    # L5
    total_points = points_from_wins + points_from_ties

    # L6
    number_of_teams = 3 # along with two other teams
    average_points = total_points / number_of_teams

    # FA
    answer = average_points
    return answer