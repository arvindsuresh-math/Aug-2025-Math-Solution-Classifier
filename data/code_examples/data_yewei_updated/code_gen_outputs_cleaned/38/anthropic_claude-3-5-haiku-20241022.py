def solve(
    mom_cup_size: int = 8,  # her mom drinks an 8-ounce cup of tea
    mom_tea_amount: int = 1,  # and uses one ounce of tea
    party_people: int = 12,  # the party has 12 people
    party_cup_size: int = 6  # each of them wants a 6-ounce cup of tea
):
    """Index: 38.
    Returns: the number of ounces of tea Artemis needs for the party.
    """
    #: L1
    total_water_volume = party_people * party_cup_size

    #: L2
    tea_ounces_needed = total_water_volume / mom_cup_size

    answer = tea_ounces_needed  # FINAL ANSWER
    return answer