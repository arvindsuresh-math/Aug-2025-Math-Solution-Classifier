def solve():
    """Index: 5328.
    Returns: the number of unique players Mona grouped with on the video game that weekend.
    """
    # L1
    num_groups = 9 # joined 9 groups
    players_per_group = 4 # four other players
    total_player_instances = num_groups * players_per_group

    # L2
    re_grouped_group1 = 2 # One of the groups included two players she had grouped with before
    re_grouped_group2 = 1 # another group included one person she had grouped with before
    total_re_grouped_instances = re_grouped_group1 + re_grouped_group2

    # L3
    unique_players = total_player_instances - total_re_grouped_instances

    # FA
    answer = unique_players
    return answer