def solve():
    """Index: 5738.
    Returns: the number of strikers in the team.
    """
    # L1
    goalies = 3 # three goalies
    defenders = 10 # ten defenders
    goalies_and_defenders = goalies + defenders

    # L2
    midfielder_multiplier = 2 # twice as many midfielders
    midfielders = midfielder_multiplier * defenders

    # L3
    total_non_strikers = midfielders + goalies_and_defenders

    # L4
    total_players = 40 # 40 players
    strikers = total_players - total_non_strikers

    # FA
    answer = strikers
    return answer