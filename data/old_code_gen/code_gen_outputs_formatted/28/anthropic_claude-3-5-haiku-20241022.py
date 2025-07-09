def solve(
    total_houses: int = 5,  # There are 5 houses on a street
    houses_with_known_gnomes: int = 4,  # First four houses have known number of gnomes
    gnomes_per_known_house: int = 3,  # Each of the first four houses has 3 gnomes
    total_gnomes: int = 20  # Total of 20 gnomes on the street
):
    """Index: 28.
    Returns: the number of gnomes in the fifth house."""

    #: L1
    gnomes_in_first_four_houses = houses_with_known_gnomes * gnomes_per_known_house

    #: L2
    gnomes_in_fifth_house = total_gnomes - gnomes_in_first_four_houses

    #: FA
    answer = gnomes_in_fifth_house
    return answer