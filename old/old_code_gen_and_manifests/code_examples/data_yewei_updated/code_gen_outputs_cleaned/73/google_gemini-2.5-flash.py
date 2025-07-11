def solve(
        pouches_per_pack: int = 6, # packs of 6 individual pouches
        team_members: int = 13, # 13 members on his baseball team
        coaches: int = 3, # 3 coaches
        helpers: int = 2 # 2 helpers
    ):
    """Index: 73.
    Returns: the number of packs of trail mix Roger needs to buy.
    """
    #: L1
    total_pouches_needed = team_members + coaches + helpers

    #: L2
    packs_to_buy = total_pouches_needed / pouches_per_pack

    answer = packs_to_buy # FINAL ANSWER
    return answer