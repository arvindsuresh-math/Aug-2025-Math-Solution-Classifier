def solve():
    """Index: 4805.
    Returns: the number of people on the island who have lost to a computer at least once.
    """
    # L1
    total_chess_players = 40 # 40 chess players
    never_lost_divisor = 4 # A quarter of the island's chess players
    never_lost_to_ai = total_chess_players / never_lost_divisor

    # L2
    lost_to_ai = total_chess_players - never_lost_to_ai

    # FA
    answer = lost_to_ai
    return answer