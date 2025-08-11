def solve():
    """Index: 38.
    Returns: the number of ounces of tea Artemis needs for the party.
    """
    # L1
    num_people = 12 # party has 12 people there
    cup_size = 6 # each of them wants a 6-ounce cup of tea
    total_water = num_people * cup_size

    # L2
    mom_cup_size = 8 # mom drinks an 8-ounce cup of tea
    ounces_of_tea_needed = total_water / mom_cup_size

    # FA
    answer = ounces_of_tea_needed
    return answer