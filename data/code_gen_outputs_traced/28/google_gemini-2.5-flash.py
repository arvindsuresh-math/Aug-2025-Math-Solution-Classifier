def solve(
        num_houses: int = 5, # There are 5 houses on a street
        num_first_four_houses: int = 4, # each of the first four houses
        gnomes_per_house: int = 3, # has 3 gnomes in the garden
        total_gnomes: int = 20 # a total of 20 gnomes on the street
    ):
    """Index: 28.
    Returns: the number of gnomes in the fifth house.
    """
    #: L1
    gnomes_in_first_four_houses = num_first_four_houses * gnomes_per_house # eval: 12 = 4 * 3
    #: L2
    gnomes_in_fifth_house = total_gnomes - gnomes_in_first_four_houses # eval: 8 = 20 - 12
    answer = gnomes_in_fifth_house # FINAL ANSWER # eval: 8 = 8 # FINAL ANSWER
    return answer # eval: return 8