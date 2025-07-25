def solve(
    total_houses: int = 5, # There are 5 houses on a street
    num_first_houses: int = 4, # each of the first four houses
    gnomes_per_first_house: int = 3, # has 3 gnomes in the garden
    total_gnomes: int = 20 # If there are a total of 20 gnomes on the street
):
    """Index: 28.
    Returns: the number of gnomes in the fifth house.
    """

    #: L1
    gnomes_in_first_four_houses = 2

    #: L2
    gnomes_in_fifth_house = total_gnomes - gnomes_in_first_four_houses

    #: FA
    answer = gnomes_in_fifth_house
    return answer