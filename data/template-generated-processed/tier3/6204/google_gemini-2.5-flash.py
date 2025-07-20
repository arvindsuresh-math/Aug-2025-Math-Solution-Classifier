def solve():
    """Index: 6204.
    Returns: the number of games the Tigers won.
    """
    # L1
    losses = 12 # 12 losses
    ties_divisor = 2 # half as many ties
    ties = losses / ties_divisor

    # L2
    total_home_games = 56 # 56 home games
    wins = total_home_games - (losses + ties)

    # FA
    answer = wins
    return answer