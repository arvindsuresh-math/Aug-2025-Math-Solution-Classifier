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
    total_water_ounces = num_people - party_cup_size # eval: 6 = 12 - 6

    #: L2
    ounces_of_tea_needed = total_water_ounces / mom_cup_size # eval: 0.75 = 6 / 8

    #: FA
    answer = ounces_of_tea_needed
    return answer # eval: return 0.75
