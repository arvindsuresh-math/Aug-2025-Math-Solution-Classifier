def solve(
        mom_cup_size: int = 8, # an 8-ounce cup of tea
        mom_tea_amount: int = 1, # uses one ounce of tea
        num_people: int = 12, # The party has 12 people
        party_cup_size: int = 6 # each of them wants a 6-ounce cup of tea
    ):
    """Index: 38.
    Returns: the total ounces of tea needed for the party.
    """

    #: L1

    #: L2
    ounces_of_tea_needed = num_people / mom_cup_size # eval: 1.5 = 12 / 8

    #: FA
    answer = ounces_of_tea_needed
    return answer # eval: return 1.5
