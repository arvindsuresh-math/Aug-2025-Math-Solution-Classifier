def solve():
    """Index: 1932.
    Returns: the total amount of money collected from the football team in 8 parties.
    """
    # L1
    fee_per_player = 40 # each football team member must pay $40
    num_players = 60 # 60 players on the football team
    amount_per_party = fee_per_player * num_players

    # L2
    num_parties = 8 # the entire team attends 8 such parties in a year
    total_amount = amount_per_party * num_parties

    # FA
    answer = total_amount
    return answer