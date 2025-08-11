def solve():
    """Index: 38.
    Returns: the total ounces of tea Artemis needs.
    """
    # L1
    num_people = 12 # The party has 12 people
    cup_size_per_person = 6 # each of them wants a 6-ounce cup of tea
    total_water_ounces = num_people * cup_size_per_person

    # L2
    mom_cup_size = 8 # her mom drinks an 8-ounce cup of tea
    tea_needed_ounces = total_water_ounces / mom_cup_size

    # FA
    answer = tea_needed_ounces
    return answer