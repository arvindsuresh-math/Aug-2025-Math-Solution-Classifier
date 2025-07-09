def solve(
    total_houses: int = 5,  # There are 5 houses on a street
    gnomes_per_first_four_houses: int = 3,  # each of the first four houses has 3 gnomes
    total_gnomes: int = 20  # total of 20 gnomes on the street
):
    """Index: 28.
    Returns: the number of gnomes in the fifth house.
    """

    #: L1

    #: L2
    gnomes_fifth_house = total_gnomes - gnomes_per_first_four_houses # eval: 17 = 20 - 3

    #: FA
    answer = gnomes_fifth_house
    return answer # eval: return 17
