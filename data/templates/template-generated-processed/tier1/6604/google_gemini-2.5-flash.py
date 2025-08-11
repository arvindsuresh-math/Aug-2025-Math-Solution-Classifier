def solve():
    """Index: 6604.
    Returns: the total number of people.
    """
    # L1
    cannoneers = 63 # 63 cannoneers
    women_multiplier = 2 # double the number of cannoneers
    num_women = cannoneers * women_multiplier

    # L2
    men_multiplier = 2 # twice the number of women
    num_men = men_multiplier * num_women

    # L3
    total_people = num_women + num_men

    # FA
    answer = total_people
    return answer