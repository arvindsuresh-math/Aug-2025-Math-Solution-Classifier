def solve():
    """Index: 577.
    Returns: the total number of sets of laces handed out.
    """
    # L1
    num_teams = 4 # 4 teams are competing
    members_per_team = 10 # each team is made up of 10 members
    total_members = num_teams * members_per_team

    # L2
    pairs_competing = 1 # 1 pair of roller skates to compete in
    pairs_backup = 1 # another pair of skates as a backup
    pairs_per_member = pairs_competing + pairs_backup

    # L3
    total_pairs = total_members * pairs_per_member

    # L4
    sets_of_laces_per_pair = 3 # 3 sets of laces per pair of skates
    total_laces = total_pairs * sets_of_laces_per_pair

    # FA
    answer = total_laces
    return answer