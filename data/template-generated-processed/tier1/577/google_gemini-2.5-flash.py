def solve():
    """Index: 577.
    Returns: the total number of sets of laces handed out.
    """
    # L1
    num_teams = 4 # 4 teams are competing
    members_per_team = 10 # 10 members
    total_members = num_teams * members_per_team

    # L2
    competing_pairs = 1 # a pair of roller skates to compete in
    backup_pairs = 1 # another pair of skates as a backup
    pairs_per_member = competing_pairs + backup_pairs

    # L3
    total_skates = total_members * pairs_per_member

    # L4
    laces_per_pair = 3 # 3 sets of laces per pair of skates
    total_laces = total_skates * laces_per_pair

    # FA
    answer = total_laces
    return answer