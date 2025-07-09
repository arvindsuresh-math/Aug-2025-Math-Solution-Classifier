def solve(
    mom_cup_size: int = 8, # her mom drinks an 8-ounce cup of tea
    mom_tea_amount: int = 1, # and uses one ounce of tea
    num_people: int = 12, # The party has 12 people there
    guest_cup_size: int = 6 # each of them wants a 6-ounce cup of tea
):
    """Index: 38.
    Returns: the total ounces of tea needed for the party.
    """

    #: L1
    total_water_ounces = num_people * guest_cup_size

    #: L2
    tea_ounces_needed = 19.0

    #: FA
    answer = tea_ounces_needed
    return answer