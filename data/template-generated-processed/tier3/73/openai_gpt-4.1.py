def solve():
    """Index: 73.
    Returns: the number of packs of trail mix Roger needs to buy.
    """
    # L1
    team_members = 13 # 13 members on his baseball team
    coaches = 3 # 3 coaches
    helpers = 2 # 2 helpers
    total_pouches_needed = team_members + coaches + helpers

    # L2
    pouches_per_pack = 6 # packs of 6 individual pouches
    packs_needed = total_pouches_needed / pouches_per_pack

    # FA
    answer = packs_needed
    return answer