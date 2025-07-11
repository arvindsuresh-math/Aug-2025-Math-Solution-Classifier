def solve():
    """Index: 1932.
    Returns: the total amount of money collected in 8 parties.
    """
    # L1
    cost_per_member = 40 # $40
    num_players = 60 # 60 players on the football team
    money_per_party = cost_per_member * num_players

    # L2
    num_parties_per_year = 8 # 8 such parties in a year
    total_money_collected = money_per_party * num_parties_per_year

    # FA
    answer = total_money_collected
    return answer