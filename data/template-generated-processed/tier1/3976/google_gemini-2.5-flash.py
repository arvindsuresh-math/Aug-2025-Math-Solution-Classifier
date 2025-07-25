def solve():
    """Index: 3976.
    Returns: the number of blocks the tower had before Jess's turn.
    """
    # L1
    num_players = 5 # The 5 players, including Jess
    blocks_per_player_per_turn = 1 # each player removes one block
    blocks_per_round = num_players * blocks_per_player_per_turn

    # L2
    num_rounds_played = 5 # play 5 rounds
    total_blocks_removed_initial_rounds = blocks_per_round * num_rounds_played

    # L3
    father_removed_block = 1 # He removes a block
    total_blocks_removed_before_jess = total_blocks_removed_initial_rounds + father_removed_block

    # L4
    initial_total_blocks = 54 # 54 stacked blocks
    blocks_before_jess_turn = initial_total_blocks - total_blocks_removed_before_jess

    # FA
    answer = blocks_before_jess_turn
    return answer