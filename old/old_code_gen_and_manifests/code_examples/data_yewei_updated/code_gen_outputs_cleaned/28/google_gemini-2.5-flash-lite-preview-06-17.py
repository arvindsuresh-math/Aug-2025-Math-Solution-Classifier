def solve(
    num_houses: int = 5, # There are 5 houses on a street
    num_gnomes_first_four_houses: int = 3, # each of the first four houses has 3 gnomes in the garden
    total_gnomes: int = 20 # If there are a total of 20 gnomes on the street
):
    """Index: 28.
    Returns: the number of gnomes in the fifth house.
    """
    #: L1
    gnomes_in_first_four_houses = 4 * num_gnomes_first_four_houses

    #: L2
    gnomes_in_fifth_house = total_gnomes - gnomes_in_first_four_houses

    answer = gnomes_in_fifth_house # FINAL ANSWER
    return answer