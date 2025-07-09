def solve(
    num_people: int = 12,  # The party has 12 people
    cup_size_party: int = 6,  # each wants a 6-ounce cup of tea
    cup_size_mom: int = 8,  # mom drinks an 8-ounce cup of tea
    tea_ounces_mom: int = 1  # mom uses one ounce of tea
):
    """Index: 38.
    Returns: the total ounces of tea needed for the party.
    """
    #: L1
    total_water_party = num_people * cup_size_party

    #: L2
    tea_needed = total_water_party / cup_size_mom * tea_ounces_mom

    answer = tea_needed  # FINAL ANSWER
    return answer