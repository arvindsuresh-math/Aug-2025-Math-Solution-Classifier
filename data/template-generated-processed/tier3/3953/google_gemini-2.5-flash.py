from fractions import Fraction

def solve():
    """Index: 3953.
    Returns: the number of goals each of the two players scored.
    """
    # L1
    total_goals_league = 300 # total number of goals scored in the league against Barca that season is 300
    percentage_by_two_players = Fraction(20, 100) # 20% of all goals scored
    goals_by_two_players = percentage_by_two_players * total_goals_league

    # L2
    number_of_players = 2 # exactly two players
    goals_per_player = goals_by_two_players / number_of_players

    # FA
    answer = goals_per_player
    return answer