def solve(
    team_members: int = 13,  # 13 members on his baseball team
    coaches: int = 3,        # plus 3 coaches
    helpers: int = 2,        # and 2 helpers
    pouches_per_pack: int = 6  # trail mix comes in packs of 6 individual pouches
):
    """Index: 73.
    Returns: the number of packs of trail mix Roger needs to buy.
    """

    #: L1
    total_pouches_needed = team_members + coaches + helpers

    #: L2
    packs_needed = total_pouches_needed / pouches_per_pack
    import math
    packs_needed_rounded = math.ceil(packs_needed)

    answer = packs_needed_rounded  # FINAL ANSWER
    return answer