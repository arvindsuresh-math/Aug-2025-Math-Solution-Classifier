def solve(
    num_players: int = 13, # Roger has 13 members on his baseball team
    num_coaches: int = 3, # plus 3 coaches
    num_helpers: int = 2, # and 2 helpers
    pouches_per_pack: int = 6 # The trail mix comes in packs of 6 individual pouches
):
    """Index: 73.
    Returns: the number of packs of trail mix Roger needs to buy.
    """

    #: L1
    total_people = num_players - num_coaches + num_helpers # eval: 12 = 13 - 3 + 2

    #: L2
    packs_needed = total_people / pouches_per_pack # eval: 2.0 = 12 / 6

    #: FA
    answer = packs_needed
    return answer # eval: return 2.0
