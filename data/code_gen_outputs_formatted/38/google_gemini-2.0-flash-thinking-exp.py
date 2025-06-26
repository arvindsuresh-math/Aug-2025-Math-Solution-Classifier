def solve(
    mom_cup_size: int = 8, # drinks an 8-ounce cup of tea
    mom_tea_amount: int = 1, # uses one ounce of tea
    num_people: int = 12, # The party has 12 people
    party_cup_size: int = 6 # each of them wants a 6-ounce cup of tea
):
    """Index: 38.
    Returns: the total ounces of tea needed for the party.
    """

    #: L1
    total_water_needed = num_people * party_cup_size

    #: L2
    total_tea_needed = total_water_needed / mom_cup_size

    answer = total_tea_needed # FINAL ANSWER
    return answer