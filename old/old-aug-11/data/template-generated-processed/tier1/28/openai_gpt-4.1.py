def solve():
    """Index: 28.
    Returns: the number of gnomes in the fifth house.
    """
    # L1
    num_first_houses = 4 # first four houses
    gnomes_per_first_house = 3 # each of the first four houses has 3 gnomes
    gnomes_in_first_four = num_first_houses * gnomes_per_first_house

    # L2
    total_gnomes = 20 # total of 20 gnomes on the street
    gnomes_in_fifth = total_gnomes - gnomes_in_first_four

    # FA
    answer = gnomes_in_fifth
    return answer