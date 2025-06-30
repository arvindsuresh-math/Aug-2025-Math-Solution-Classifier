def solve(
    team_members: int = 13,  # Roger has 13 members on his baseball team
    coaches: int = 3,  # plus 3 coaches
    helpers: int = 2,  # and 2 helpers
    pouches_per_pack: int = 6  # trail mix comes in packs of 6 individual pouches
):
    """Index: 73.
    Returns: the number of packs of trail mix Roger needs to buy."""

    #: L1
    total_pouches_needed = team_members + coaches + helpers # eval: 18 = 13 + 3 + 2

    #: L2
    packs_needed = total_pouches_needed / pouches_per_pack # eval: 3.0 = 18 / 6

    #: FA
    answer = packs_needed # eval: 3.0 = 3.0
    return answer # eval: return 3.0
