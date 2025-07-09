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
    total_people = team_members * coaches + helpers # eval: 41 = 13 * 3 + 2

    #: L2
    packs_needed = total_people / pouches_per_pack # eval: 6.833333333333333 = 41 / 6

    #: FA
    answer = packs_needed
    return answer # eval: return 6.833333333333333
