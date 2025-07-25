def solve(
    num_people: int = 12,  # The party has 12 people there
    cup_size_party: int = 6,  # each of them wants a 6-ounce cup of tea
    cup_size_mom: int = 8,  # mom drinks an 8-ounce cup of tea
    tea_ounces_mom: int = 1  # mom uses one ounce of tea
):
    """Index: 38.
    Returns: the total ounces of tea needed for the party.
    """

    #: L1
    total_ounces_water = num_people * cup_size_party # eval: 72 = 12 * 6

    #: L2
    ounces_tea_needed = total_ounces_water / cup_size_party * tea_ounces_mom # eval: 12.0 = 72 / 6 * 1

    #: FA
    answer = ounces_tea_needed
    return answer # eval: return 12.0
