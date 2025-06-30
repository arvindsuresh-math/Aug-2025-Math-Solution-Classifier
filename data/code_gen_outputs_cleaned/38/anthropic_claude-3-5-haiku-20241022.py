def solve(
    mom_cup_size: int = 8,  # her mom drinks an 8-ounce cup of tea
    mom_tea_amount: int = 1,  # uses one ounce of tea
    party_guests: int = 12,  # the party has 12 people
    guest_cup_size: int = 6  # each of them wants a 6-ounce cup of tea
):
    """Index: 38.
    Returns: the total number of ounces of tea needed for the party."""
    #: L1
    total_water_volume = party_guests * guest_cup_size

    #: L2
    total_tea_needed = total_water_volume / mom_cup_size

    answer = total_tea_needed  # FINAL ANSWER
    return answer