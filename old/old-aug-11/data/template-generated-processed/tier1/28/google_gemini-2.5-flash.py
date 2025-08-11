def solve():
    """Index: 28.
    Returns: the number of gnomes the fifth house has.
    """
    # L1
    num_first_four_houses = 4 # first four houses
    gnomes_per_house = 3 # 3 gnomes in the garden
    gnomes_first_four_houses = num_first_four_houses * gnomes_per_house

    # L2
    total_gnomes = 20 # a total of 20 gnomes on the street
    gnomes_fifth_house = total_gnomes - gnomes_first_four_houses

    # FA
    answer = gnomes_fifth_house
    return answer