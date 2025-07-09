def solve(
    pouches_per_pack: int = 6, # The trail mix comes in packs of 6 individual pouches
    team_members: int = 13, # Roger has 13 members on his baseball team
    coaches: int = 3, # plus 3 coaches
    helpers: int = 2 # and 2 helpers
):
    """Index: 73.
    Returns: the number of packs of trail mix Roger needs to buy.
    """

    #: L1

    #: L2
    packs_needed = team_members / pouches_per_pack

    #: FA
    answer = packs_needed
    return answer