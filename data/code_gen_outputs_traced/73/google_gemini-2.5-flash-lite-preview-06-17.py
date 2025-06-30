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
    total_people = num_players + num_coaches + num_helpers # eval: 18 = 13 + 3 + 2
    #: L2
    packs_needed = total_people / pouches_per_pack # eval: 3.0 = 18 / 6
    answer = packs_needed # FINAL ANSWER # eval: 3.0 = 3.0 # FINAL ANSWER
    return answer # eval: return 3.0